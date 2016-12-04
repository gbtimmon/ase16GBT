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
| SA        | 14.8                             |
| MWS       | 9.2                              |
| DE        | 16.9                             |

As shown in the table, Simulated Annealing has the smallest number of early termination. However, Simulated Anealing is continuously updating just one candidate by jumping randomly. It's doubtful that Simulated Anealing may not be able to get a better value and then keeping it's current value for a long time and in the end early terminated. 

As shown in the table, Max-WalkSat has the smallest number of eras to terminate the program. The reason resides in the design of algorithm: every time after a random jump, Max-WalkSat has a probability to do local search to maximize the score in one of the directions. This will give it a high quality of candidates, which will also result in the algorithm getting it's best score at the early stage. 

Simulated Annealing, on the other hand, just perform random jump and jump to lower optimized point depending on a cooling function. Hence, the best candidates is more frequently updated in this function than Max-WalkSat. When it changes a lot, A12 function will conclude that the candidates in current era is still changing and then give the algorithm more lives to move on. Hence, Simulated Annealing is doing much worse than Max-WalkSat in early terminating the program.

For Differential Evolution, as it keep a population as a frontier (in our experiment, the population size is equal to the era size which is 50), each candiate performing mutation individually. As a multi-objecitve optimizer, it provide better exploration rate than the other two algorithms. However, when the exploration rate increases, the candidate will continuously updating the best candidate it found. Hence, A12 function will also judge the population in current era is changing. An optional way to construct the era might be to find the best candidate in each update. Then the era can be constructed with an array of size 50 containing the best candidate found in each update. The optional way to perform comparison may dramatically decrease the number of eras in Differential Evolution. 


### Comparison of three optimizers depending on the cdom loss

```

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,          mws ,    0.14  ,  1.17 (           --*-|              ), -0.26,  0.16,  0.90
   1 ,           de ,    0.19  ,  1.55 (           --*-|-             ), -0.38,  0.21,  1.17
   1 ,           sa ,    0.39  ,  1.21 (           ---*|              ), -0.26,  0.42,  0.95

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           de ,    0.31  ,  1.56 (           ---*|-             ), -0.56,  0.39,  1.00
   1 ,          mws ,    0.32  ,  1.72 (           ---*|--            ), -0.47,  0.34,  1.25
   1 ,           sa ,    0.50  ,  1.68 (           ----*--            ), -0.35,  0.61,  1.33

rank ,         name ,    med   ,  iqr 
----------------------------------------------------
   1 ,           de ,    0.70  ,  1.22 (       -*-     |              ), 0.40,  0.74,  1.62
   1 ,          mws ,    0.87  ,  1.54 (      --*-     |              ), -0.05,  0.98,  1.49
   1 ,           sa ,    1.03  ,  1.73 (      ---*-    |              ), 0.11,  1.08,  1.84


```


As shown in the table, all three algorithms have the same rank with each of them doing good in different areas.

- Differential Evolution: the performance of Differential Evolution is pretty good. It is not as stable as Max-WalkSat because each individual inside the population follow their own ways to mutate, which is time consuming to get convergence (move to heaven). However, if more eras is given, the performance of Differential Evolution is expected to be increasingly better. The reason is Differential Evolution explore the landscape, or the problem, better than the other two single objective algorithms.

- Max-WalkSat: at a probability, Max-WalkSat performs better than Differential Evolution. This is because of all the three algorithms do not ensure to provide the best solution or how good the solution is. Due to the local search ingredient in Max-WalkSat, it can explore the landscape better than Simulated Annealing in the same amount of era. Hence, the performance of Max-WalkSat will be highly possibily to be better than Simulated Annealing. 

- Simulated Annealing: as for Simulated Annealing, there is anohter drawback found in this experiment. The result of Simulated Annealing is wider spread than the other two algorithms. This indicate that the algorithm is not as stable as the others to provide a good solution. 

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


