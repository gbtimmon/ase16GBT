# Comparison of Simulated Annealing, MaxWalkSat, and Differential Evolution with DTLZ7 as the model

## Abstract
Conventional methods arrive at optimal solution by compairng all the possible candidate solutions, which cause the time complexity grows   exponentially with the size of the data.
<br>This practice attempts to compare the performance of Simulated Annealing, MaxWalkSat, and Differential Evolution by running them on the DTLZ7 model with 10 decision variables and 2 objective functions. To compare the performance among the optimizers, statistical machinery like bootstrapping, a12, and Scott-Knott were used.

## Introduction
In this section, all the algorithms used in this experiment has been described and discussed. They are **Simulated annealing**, **Max-WalkSat**, **Differential Evolution**,  **3 Types of Comparison**

### Simulated Annealing
Simulated annealing optimizes model by keeping state of 3 different candidates which include best solution, last solution and current solution. It works by making random jumps across the decision space and comparing to the last solution as well as the best solution. With a cooling function that decreases the possibility to jump to a point that is lower optimized when the number of generation increases, Simulated Annealing jumps to sub-optimal solutions. The idea behind this is that jumping out of the local best solution trap and moving towards a globally optimal solution in later iterations.
```
* A baseline study to find minimum and maximum points
* In each generation, generate a new model with randomized candidates
* Type 1 comparison is performed between the best solution and new candidate 
    * If the new candidate is better update best solution
* Type 1 comparison is performed between the new candidate and local solution
    * If the new candidate is better update local solution
* After the era size
    * Type2 comparison between era and era - 1
    * If no changing detected, reduce lives left
    * else, give more lives
* Exit 
    * if ran out of lives
    * if ran out of generations
```



