# Early Termination of Simulated Annealing, MaxWalkSat, and Differential Evolution with DTLZ7 as the model

## Abstract
Conventional methods arrive at optimal solution by compairng all the possible candidate solutions, which cause the time complexity grows   exponentially with the size of the data. In this report, three metaheuristics approaches has been discussed and compared. They can quickly provide a solution and continuously improve it. Those approaches do not guarantee an optimal solution is ever found.

This practice attempts to use 3 types of comparison operators to early terminate Simulated Annealing, MaxWalkSat, and Differential Evolution by running them on the DTLZ7 model with 10 decision variables and 2 objective functions. A comparison of the three optimizers will be discussed as well. 

To compare the performance among and inside the optimizers, statistical machinery like bootstrapping, a12, and Scott-Knott were used. 

## Introduction
In this section, all the algorithms used in this experiment has been described and discussed. They are **Simulated annealing**, **Max-WalkSat**, **Differential Evolution**,  **3 Types of Comparison**, **Scott-knott**

### Simulated Annealing
Simulated annealing optimizes model by keeping state of 3 different candidates which include best solution, last solution and current solution. It works by making random jumps across the decision space and comparing to the last solution as well as the best solution. Simulated Annealing jumps to sub-optimal solutions with a cooling function that decreases the possibility when the number of generation increases. The idea behind this is that jumping out of the local best solution trap and moving towards a globally optimal solution in later iterations.

```
* A baseline study to find minimum and maximum points
* while still have lives and does not run out of generations
    * generate new candidate
    * Type 1 comparison is performed between the best solution and the new candidates
        * If the new candidate is better, update best solution and the last solution
    * Type 1 comparison is performed between the last solution and the new candidates
        * If the new candidate is better, update the last solution
    * After the era size
        * Type2 comparison between era and era - 1
        * If no changing detected, reduce lives left
        * else, give more lives
```

### Max-WalkSat
MaxWalkSat is a non-parametric stochastic method for landscape sampling sampling. In large search, landscape can be complex with a number of traps, for example, saddles, holes and poles. Thus, it makes progress by combining local search and retries which provide a good trade-off between finding global optimal and escaping from traps. Compared to Simulated Annealing, Max-WalkSat has a landscape exploration bit. 


```
* while still have lives and number of tries is less than retries
    * A new candidate is generated
    * while number of changes is less than maximum changes
        * If mutation_prob satisfied
            * One of the decisions is randomly mutated
        * If not 
            * local search with type1 comparison to maximize one of the directions
        * Type 1 comparison is performed between the best solution and the new candidates
            * If the new candidate is better, update best solution
    * After the era size
        * Type2 comparison between era and era - 1
        * If no changing detected, reduce lives left
        * else, give more lives
```

### Differential Evolution
Differential evolution is a multi-objective optimizer. It optimizes a problem by maintaining a population of candidate solutions and improving it. DE optimizes a problem by treating it as a black box and only use the quality measurement provided by the candidates so the gradient is not needed. Compared with the former two optimizers, it can search very large spaces of candidate solutions.

DE/rand/1 has been used in this practice.

* DE
```
* Generate an frontier that contains a size of initial candidates
* while still have lives and does not run out of generations
    * update the current frontier
    * After the era size
        * Type2 comparison between era and era - 1
        * If no changing detected, reduce lives left
        * else, give more lives
```

* Update frontier
```
* for each candidate in frontier
    * extrapolate candidate
    * Type 1 comparison is performed between the candidate in frontier and the new candidates
         * If the new candidate is better, update the frontier
* return frontier and cur ear scores
```

* extrapolate
```
* picks 3 different random candidates: two three, and four from frontierand 
* while the new candidate is not legal
   * for each decision
         * mutates the decision with two, three and four based on a cross over factor with a possibility
   * if all the decisions remain the same
         * assign one decision from two to one
```

### Type1 Comparison

Type 1 operator was implemented to compare the domination of an individual solution over other. To establish dominance, it compares median performance scores provided by the model. The summation of each objective has been used as the performance score. 

### Type2 Comparison

Type2 operator was implemented to compare two sets of eras. It was used to measure of how different one era is from the other. The operator takes the current era and the previous era to calculate the difference between the two. Early termination for the algorithm happens when the optimizer runs out of lives. A12 was used To calculate the difference between eras. the A12 statistics measures the
probability that running algorithm *X* yields higher values than running another algorithm *Y*.According to Vargha and Delaney, a small, medium, large difference between two populations is:

-   *large* if `a12` is over 71%;
-   *medium* if `a12` is over 64%;
-   *small* if `a12` is 56%, or less.  [1]

Here we consider a small effect so we set threshold to 0.56.

```3
    * Sort the values for solutions in era and era - 1
    * Run A12 test to check for difference
    * if improvement > 0.56
         * add 5 more lives
    * else
         * reduce 1 life
```

### Type3 Comparison

Type3 operator was implemented to compare the final eras between multiple optimizers. 1000 bootstraps was used with A12 and s. The rdivdemo program creates graphs which show the median, the inter quartile range and the 25 %ile , 50 %ile amd 70 % ile values .

```
    *  run Simulated Annealing, MaxWalkSat, and Differential Evolution for 20 repeats
        * For each repeat
             * Run each optimizer and save the cdom loss between era0 the final era
    Statistical Analysis of Scott-Knott,a12 and rank the optimizers
```

### Continuous Domination 

What _cdom_ does is that it takes the differences between each objective, then
raises it to a exponential factor. From this we compute the mean loss the loss in travelling
Formally, this is a domination test across the Pareto frontier. [2]

```python
def (i):      # return less for minimize and more for maximize
def norm(i,x): # returns (x - lo) / (hi - lo) where lo and hi
               # are the min,max values for objective i

def better(this, that):
  x  = scores[ id(this) ]
  y  = scores[ id(that) ]
  l1 = loss(x,y)
  l2 = loss(y,x)
  return l1 < l2 # this is better than that if this losses least.

def loss(x, y):
  losses= 0
  n = min(len(x),len(y))
  for i,(x1,y1) in enumerate(zip(x,y)):
    x1 = norm(i,x1) # normalization
    y1 = norm(i,y1) # normalization
    losses += expLoss( i,x1,y1,n )
  return losses / n  # return mean loss

def expLoss(i,x1,y1,n):
  "Exponentially shout out the difference"
  w = -1 if minimizing(i) else 1 # adjust for direction of comparison
  return -1*math.e**( w*(x1 - y1) / n ) # raise the differences to some exponent
```  



### Scott-knott

The Scott & Knott method make use of a cluster analysis algorithm, where, starting from the whole group of observed mean effects, it divides, and keep dividing the sub-groups in such a way that the intersection of any two groups formed in that manner is empty [3]

## Results

### Counts of Earlty termination
| Optimizer | Avg. No. eras before termination |
|-----------|----------------------------------|
| SA        | 13.6                             |
| MWS       | 14.6                             |
| DE        | 13.9                             |

As shown in the table, Simulated Annealing has the smallest number of early termination. However, Simulated Anealing is continuously updating just one candidate by jumping randomly. It's doubtful that Simulated Anealing may not be able to get a better value and then keeping it's current value for a long time and in the end early terminated. 

For the other two algorithm:

- Differential Evolution is keeping a population with size of 50. The quality of each candidate will get update in each era which is not helping it to terminate quicker than Simulated Annealing. 

- Max-WalkSat will do local search at a probability after the random jump, which will give it higher possibility to get a better value while searching. By frequently updating the solution, it will continuously getting more lives and as a result, hard to early terminate. 


### Comparison of three optimizers depending on the cdom loss

```
rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           de ,    -1.70  ,  1.04 (               |     --*---   ), -2.06,  -1.69,  -1.03
   1 ,           sa ,    -1.35  ,  0.93 (               |      ----*   ), -2.01,  -1.31,  -1.08
   1 ,          mws ,    -1.29  ,  0.50 (               |         -*-  ), -1.44,  -1.28,  -0.94

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           de ,    -1.35  ,  1.52 (               |           --*), -2.57,  -1.35,  -1.05
   1 ,           sa ,    -1.32  ,  1.10 (               |            -*), -2.15,  -1.30,  -1.04
   1 ,          mws ,    -1.06  ,  1.05 (               |            -*), -1.95,  -1.03,  -0.91

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           sa ,    -1.49  ,  1.28 (               |     ----*--  ), -2.15,  -1.47,  -0.88
   1 ,           de ,    -1.35  ,  0.96 (               |     ----*-   ), -2.05,  -1.33,  -1.09
   1 ,          mws ,    -1.21  ,  0.61 (               |        --*   ), -1.57,  -1.19,  -0.96

```

As shown in the table, Differential Evolution works best on DTLZ 7 with 2 objectives and 10 decisions followed by Max-WalkSat then Simulated Annealing. Since we are comparing continuous domination loss numbers generated between the first era and final era, this indicates that DE produces the best loss.

As shown in the table, all three algorithms have the same rank with each of them doing good in different areas.

- Simulated Annealing: as discussed above, it has the smallest number of eras to get early terminated. However, as can be seen in the table, the results in each repeat of Simulated Anealing is quite wide spreaded, which suggests that the algorithm is not very stable. 

- Max-WalkSat on the other hand, it very stable. All of the results tend to fall in a pretty narrow range. However, the performance of Max-WalkSat is not as good as expected. This may due to the limited number of eras provided in the experiment or a bad luck.

- Differential Evolution: the performance of Differential Evolution is pretty good. It is not as stable as Max-WalkSat because each individual inside the population follow their own ways to mutate, which is time consuming to get convergence (move to heaven). However, when more eras is given, the performance of Differential Evolution is expected to be increasingly better. The reason is Differential Evolution explore the landscape, or the problem, better than the other two single objective algorithms.

## Threats to Validity

*  the optimizer search for the solution stochastically. They do not guarantee an optimal solution can be found but they can reduce the time complexity and provide high probability to get a solution that is very close to the optimal one.

* Running the code for a larger number of iterations may produce a more convincing result. 

* As the three optimizers use different ways in searching, it is difficult to control the number of generations to make the comparison fair.

* By this experiment, Differential Evolution seems to be the most efficient and effective optimizer. Howerver, it is a mistake to conclude that Differential Evolution can take the place of the other two optimizers in optimizing models. All the three algorithms have different suitable use case. For example, Simulated Annealing is useful when the memory space is limited. Each algorithm may also behave differently when searching for different landspace. 

* The exploration rate of the searching space is not considered.

## Future Work

* This practice only used one model with fixed number of decisions and objectives. This can be expanded to multiple model with various number of decisions and objectives, which will provide more considerable results. 

* The evaluation can also be expanded from merely score of objectives to time taken in each generation and rate of space explored in the model. 

* Genetic Algorithm can also be included in this practice. 

* A research can be established to find specific constraints to provide better fairness when running three different optimizers. 


## Reference
[1] https://github.com/txt/ase16/blob/master/src/stats.py
<br>[2] https://github.com/txt/ase16/blob/master/doc/perform.md
<br>[3] https://rdrr.io/cran/ScottKnott/man/ScottKnott-package.html


