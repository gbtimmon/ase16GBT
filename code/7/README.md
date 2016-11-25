# Comparison of Simulated Annealing, MaxWalkSat, and Differential Evolution with DTLZ7 as the model

## Abstract
Conventional methods arrive at optimal solution by compairng all the possible candidate solutions, which cause the time complexity grows   exponentially with the size of the data. In this report, three metaheuristics approaches has been discussed and compared. They can quickly provide a solution and continuously improve it. Those approaches do not guarantee an optimal solution is ever found.
<br>This practice attempts to compare the performance of Simulated Annealing, MaxWalkSat, and Differential Evolution by running them on the DTLZ7 model with 10 decision variables and 2 objective functions. 
<br>To compare the performance among the optimizers, statistical machinery like bootstrapping, a12, and Scott-Knott were used. 

## Introduction
In this section, all the algorithms used in this experiment has been described and discussed. They are **Simulated annealing**, **Max-WalkSat**, **Differential Evolution**,  **3 Types of Comparison**

### Simulated Annealing
Simulated annealing optimizes model by keeping state of 3 different candidates which include best solution, last solution and current solution. It works by making random jumps across the decision space and comparing to the last solution as well as the best solution. With a cooling function that decreases the possibility to jump to a point that is lower optimized when the number of generation increases, Simulated Annealing jumps to sub-optimal solutions. The idea behind this is that jumping out of the local best solution trap and moving towards a globally optimal solution in later iterations.

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

### Type2

Type2 operator was implemented to compare two sets of eras. It was used to measure of how different one era is from the other. The operator takes the current era and the previous era to calculate the difference between the two. Early termination for the algorithm happens when the optimizer runs out of lives. A12 was used To calculate the difference between eras. the A12 statistics measures the
probability that running algorithm *X* yields higher values than running another algorithm *Y*.According to Vargha and Delaney, a small, medium, large difference between two populations is:

-   *large* if `a12` is over 71%;
-   *medium* if `a12` is over 64%;
-   *small* if `a12` is 56%, or less.  [1]

Here we consider a small effect so we set threshold to 0.56.

```
    * Sort the values for solutions in era and era - 1
    * Run A12 test to check for difference
    * if improvement > 0.56
        * add 5 more lives
    * else
         * reduce 1 life
```



## Reference
[1] https://github.com/txt/ase16/blob/master/src/stats.py
