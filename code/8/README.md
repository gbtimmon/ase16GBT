# Implementation of NSGA-II

## Abstract
Homework 8 involves implementing the NSGA-II algorithm using both Binary and Continuous domination methods. The goal was
to test which one performed better across a selection of DTLZ test problems. After running the optimizer over both domination
methods using DTLZ 1, 3, 5, and 7 with 2, 4, and 6 objectives along with 10, 20, and 40 decisions, we found that there 
was not much difference in performance between binary and continuous domination tactics. This goes against our hypothesis
that continuous domination would out-perform binary domination as the number of objectives increased in each problem space.
In the future we think that significantly increasing the objective space may lead to more significantly different solutions
as binary domination will struggle to produce valuable results across so many objectives. 

## Introduction
In this section of Homework the goal was to implement our own version of NSGA-II using knowledge from lectures and implement it
using two versions of comparisons: binary domination (bdom) and continuous domination (cdom). We ran the algorithm against some
of the DTLZ equations, models designed to test optimization algorithms.

## NSGA-II Algorithm
The NSGA-II Algorithm is a multi-objective evolutionary algorithm (MOEA) that takes advantage of a fast non-dominated sorting approach<sup>[1]</sup>.
NSGA-II is an improvement to an original NSGA algorithm. NSGA-II uses crowding distance algorithm to find solutions that are densely 
populated around a specific area and works to spread out the solutions across the objective space. 

![NSGA-II Visualization](http://i.imgur.com/VkbVbTi.gif)

The process of NSGA-II is illustrated in the above image. First a collection of children solutions are produced from the
parent population. Then the collection of candidate solutions are split into different frontiers based on their
performance in a non-dominated sort. After being separated, the candidates are trimmed back down to a manageable
population size by selecting the best frontiers and using a crowding distance sort to take the best part of
candidates from the last frontier. Then the population is ready to produce new children again and go through
the same fitness process.

### Binary Domination with Cuboid Sorting
In binary domination, a candidate dominates another candidate when the following things happen<sup>[4]</sup>:

* If at least one objective score is better
* No objective is worse than the other candidate

The following code is an excerpt of the binary domination algorithm from our project<sup>[3]</sup>:

```python
def bdom(problem, one, two):
    """
    Return if one dominates two based
    on binary domintation
    """
    objs_one = problem.evaluate(one)
    objs_two = problem.evaluate(two)
    dominates = False
    for i, obj in enumerate(problem.objectives):
        better = lt if obj.do_minimize else gt
        if better(objs_one[i], objs_two[i]):
            dominates = True
        elif objs_one[i] != objs_two[i]:
            return False
    return dominates
```

The code starts by evaluating each objective in order to obtain the latest score for each. Then the code
iterates through each objective in the problem and tests whether the score of the first candidate is better than the
score of the second. If it is then dominates is marked as True. However, if there is a case where the objectives fail
the better test and are not equal, that means that an objective on the second candidate is better than the first so
the domination will fail immediately by returning False.  

### Continuous Domination

One downside to binary domination is that it will only tell whether or not a point dominates another, but not by how
much<sup>[4]</sup>. With continuous domination, callers will receive information on how much a candidate dominates
another. For instance, if there are a few objectives that perform worse on one candidate but one objective where it
performs significantly better, then continuous domination will take each difference into account with a cumulative total
domination score. By looking at the overall picture, candidates are more likely to sacrifice some smaller score
differences in order to take a huge gain in another area. 

In addition to the scoring differences, continuous domination performs even better than binary domination when the 
number of objectives increases. With many objectives, it becomes harder for one candidate to outscore another on every 
single objective. With continuous domination, the algorithm takes into account the differences across all objectives
and come to a conclusion every time.

```python
def exp_loss(problem, i, x, y, n):
    w = -1 if problem.objectives[i].do_minimize else 1
    return -1 * math.e**(w * (x - y) / n)


def loss(problem, x, y):
    losses = 0
    n = min(len(x), len(y))
    for i, (x1, y1) in enumerate(zip(x, y)):
        losses += exp_loss(problem, i, x1, y1, n)
    return losses / n  # return mean loss


def cdom(problem, one, two):
    x = []
    y = []
    for i, (xobj, yobj) in enumerate(zip(one.objectives, two.objectives)):
        x.append(problem.objectives[i].normalize(xobj))
        y.append(problem.objectives[i].normalize(yobj))
    l1 = loss(problem, x, y)
    l2 = loss(problem, y, x)
    return l1 < l2   # l1 is better if it losses least
```

In the above code cdom() is called initially. First it will normalize the objectives so everything will compare on the 
same playing field. Then it will call a loss function on both sets of objectives. If the first candidate has the least 
losses then it will be the better performing candidate. In the loss function the differences between the two problems 
are raised to an exponent and added to a running total, which is then returned as a mean across all objectives. The 
reason we have an exponent is to make the differences more dramatic between two candidates. 


## DTLZ
In order to test how NSGA-II performs, a problem set must be created. The set must also be flexible in its number of 
decisions and objectives in order to test different aspects of the optimizer. For such a purpose a test suite called 
DTLZ was created. DTLZ uses a variety of different functions to create different flexible scenarios to run an optimizer 
against.<sup>[2]</sup>

### DTLZ 1

![DTLZ 1](http://i.imgur.com/ZFzvySo.png)

The difficulty of DTLZ 1, whose functions are listed above, is to converge onto a hyper-plane<sup>[2]</sup>. 

### DTLZ 3

![DTLZ 3](http://i.imgur.com/p3i6aut.png)

DTLZ 3's functions are listed above. The design of these functions are to introduce many local Pareto-optimal fronts 
that are parallel to the global front where an optimizer may get stuck<sup>[2]</sup>. 

### DTLZ 5

![DTLZ 5](http://i.imgur.com/4vflqVj.png)

DTLZ 5 was designed to test whether an optimizer could converge on a curve. It also allows for an easier way to visually
demonstrate it's performance by plotting f<sub>M</sub>(shown above) with any other objective function<sup>[2]</sup>.

### DTLZ 7

![DTLZ 7](http://i.imgur.com/1kYWjEh.png)

DTLZ 7 is unique because it offers 2<sup>M-1</sup> disconnected Pareto-optimal regions in the space. The problem is 
designed to test the optimizer's ability to maintain sub-populations in the different Pareto-optimal 
regions<sup>[2]</sup>.

## Results
Across all DTLZ models the scores between binary domination and continuous domination are fairly similar. With 20 
retries, the differences seem to be negligible. The hyper-volume averages below have been normalized by dividing each 
hyper-volume by the number of objectives that were tested as the hyper-volume would grow with an increased number of 
objectives. Even after normalized, most of the hyper-volume scores were better for higher number of objectives. 

### DTLZ 1
As seen in the results below, with each increase in objectives, the score increases as well, even after normalizing 
across objectives. For this problem set the number of decisions does not play a significant role in the difference of 
scores.

![DTLZ 1 Results](http://i.imgur.com/r1ZaDPo.png)

### DTLZ 3
With DTLZ 3, the results are a little more hazy. On average, the higher the number of objectives the better it performs 
but there were some outliers which did not perform the same. One example is 6 objectives and 40 decisions with cdom 
which performed much worse than all the other 6 objective runs. 

![DTLZ 3 Results](http://i.imgur.com/hTewiSb.png)

### DTLZ 5
In the DTLZ 5 equation the clear winner for hyper-volume scores was using two objectives which outperformed both 4 and 
objectives for all number of decisions. Both 4 and 6 objectives performed about the same on average. 

![DTLZ 5 Results](http://i.imgur.com/chHsvuW.png)

### DTLZ 7
Performance for DTLZ 7 was very similar across all numbers of objectives and decisions. This may be due to most of the 
objectives just using on value so there may not be as much variability. 

![DTLZ 7 Results](http://i.imgur.com/qbrxkEJ.png)

## Threats to Validity

Despite having findings in our process of implementing NSGA-II there may be threats to the validity of our results and 
conclusions. One of the biggest indicators of a problem was our finding that there was not a significant difference in 
performance between binary and continuous domination. According to lecture notes on performance, continuous domination 
should have performed better as more objectives were added to the problem space<sup>[4]</sup>. However, our results 
indicate that there was no significant difference between the two comparison methods. In fact, from a timing 
perspective, cdom ran slower than bdom and did not provide any significant advantage as a result. 

Another potential threat was the use of only one metric to test whether a solution was good or not. Due to time 
constraints, our team only implemented the hyper-volume metric. While a good indicator of a successfully formed pareto 
frontier, the hyper-volume may not be capable of telling the whole story alone. Metrics like spread and igd would be 
helpful to determine whether a set of candidate solutions were evenly distributed along the pareto frontier and close to
an ideal solution<sup>[4]</sup>. Without this information, we don't have a complete picture on whether our results are 
truly the best of the best when it comes to finding ideal candidate solutions. 

## Future Work
The most immediate future work that needs focus is to continue to increase the number of objectives in the problem space
to see if continuous domination will emerge as a clear leader in comparison methods. We felt that in order really see 
how they perform we should significantly ramp up the number of objectives to something like 20 - 30 to really strain 
the comparison methods. We predict that with that many objectives it would be difficult to totally dominate another 
solution using bdom and the continuous domination method might offer a better way to sort through the solutions. 

Another area to perform future work is to increase the number of metrics to analyze the solutions. With only 
hyper-volume we will not have a complete picture of the problem space. Adding spread and igd will help to complete 
the picture.

Finally, we think that a comparison between time and strength of solutions would be something worth investigating. 
Perhaps while running NSGA-II each generation of solutions could be saved and compared with other generations over time. 
Our prediction is that there is a sweet-spot of generations that will really help to balance the time investment with the 
solution space and would produce something good enough without being the best it could produce. Perhaps an easier path 
would be to vary the number of generations in addition to varying the objectives and decisions. 

## References
[1] http://ieeexplore.ieee.org.prox.lib.ncsu.edu/document/996017/
<br> [2] http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf
<br> [3] Binary Domination code taken from GA class workshop
<br> [4] https://github.com/txt/ase16/blob/master/doc/perform.md
