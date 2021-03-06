# Optimizing the Optimizer: Using DE to optimize GA

## Abstract
In this homework we were asked to use Differential Evolution to optimize default values for a Genetic Algorithm so it 
would produce better solutions in it's optimization. We hooked GA into the Problem workshop code from previous classes 
and used that to run DE<sup>[2]</sup>. In our results, we found that the tuned GA ran significantly better than the 
un-tuned GA. However, we are worried that limiting the population size and number of retries for our DE may have 
interfered with the potential of our solutions. 

## Introduction
In this part of the homework, the goal was to optimize the defaults of the Genetic Algorithm (GA) by running it through 
an instance of differential evolution. We hypothesize that by tuning the GA it will perform better against an un-tuned 
version of the GA with the usual defaults. 

## DE
Differential Evolution is a multi objective optimizer. It optimizes a problem by maintaining a population of candidate 
solutions and improving it. In order to optimize problems, DE treats the problem as a black box and uses the quality 
measurements provided by the problem itself to determine whether a solution is better than a previous 
solution<sup>[1]</sup>. 

For our implementation of DE, we would extrapolate a new solution based on the other candidates in the population. By 
selecting 3 other solutions we could come up with a new decision that was random but loosely based on other candidates 
so we do not have to reinvent the wheel in finding good new solutions. However, we were able to overcome local optima by 
adding in the random jump in decision space.

## GA

For this problem we used the Genetic Algorithm provided in the code workshop as our basis of the problem<sup>[2]</sup>. 
We configured a Problem to take on a GA. The decisions we optimized for were mutation rate, crossover rate, population 
size and number of generations. On a baseline run of GA, the defaults we use are 0.01 for mutation rate, 0.9 for 
crossover rate, 100 for population size and 250 for generations.

For mutation rate we decided on a range between 0.01 and 0.1. We wanted to keep the mutation rate somewhat lower so it 
would not mutate the entire population at once and throw away any progress towards an ideal solution. We varied the 
crossover rate between 0.1 and 1.0. We felt that any range of crossover could produce different kinds of results. If we 
had a slowly changing population it might choose other factors to optimize for. 

For population size, we went with a range between 20 and 200. We wanted the population to have a large enough size to 
effectively crossover between, but we also wanted to keep it under 200 to help limit the runtime for the problem. 
Finally we decided on a range of 10 to 250 for the number of generations. We were curious to see if limiting the 
number of generations would have an effect on how well the solutions would perform but we also did not want to use too 
many generations in the interest of limiting runtime. 

```python
    def simulate(self, decisions):
        from ga import ga
        problem = self.dtlz_func(self.num_objectives, self.num_decisions)
        inital, final = ga(problem=problem, mutation=decisions[0], crossover_rate=decisions[1],
                           pop_size=int(decisions[2]), gens=int(decisions[3]))
        # we would calculate hypervolume
        write_results('ga_results.txt', problem, final)
        return get_hypervolume_list() 

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives
```

The snippet of code above is the evaluation method of the GA Problem. Each point will be evaluated by running the 
optimizer with the selected decisions and the results were scored using the hyper-volume of the solution. The issue with 
running a new GA with every candidate solution was the time constraint. When the problem expanded the runtime inflated 
significantly so we had to be careful to use measures to limit the runtime.

## Results
We were surprised to find in our results how well the optimization performed on the GA. The results of the solutions are 
detailed below. The Baseline run is how GA performs using 5 retries on the original defaults for the algorithm. 
The initial population are the candidates with randomly generated decisions and the final populations are the solutions 
after being optimized for hyper-volume.

![Running DE on GA Results](http://i.imgur.com/apjE5X2.png)

As shown in the results the final population performed significantly better than the initial and much better than the 
baseline of GA. What was rather unusual was in each run of DE we always had one candidate that performed worse than the 
others, shown here with a hyper-volume of 1.5 compared to the median of 4.86. We predict that this candidate may have
gotten stuck in a local optimal solution and did not have the time to mutate out of it. However, even the worst of the
final candidate solutions outperformed the best of the baseline runs. 


## Threats to Validity
In the results, the baseline run shows that there is a large variety of hyper-volumes based off of just one set of 
defaults. Because of this, we fear that running the GA just once per candidate solution may not be the best approach 
due to the variability. 

We only used one metric to score the candidate solutions due to time constraints. Introducing more metrics might change 
the results of the optimization of GA as more factors are introduced. 

We spent a lot of time limiting the runtime of the algorithm because of its potential to scale the time up as more 
factors were introduced. 

We kept the population maintained by the GA to a small population of 5 candidate solutions. We think that this might 
have interfered with the results as it limited the diversity across the solutions. However, increasing the population 
space would have significantly increased the runtime of the algorithm as it would have to run GA many more times for 
each new population member.

Similar to the concern for the population size we limited the number of retries to 10 in order to help save runtime. 

## Future Work
Given more time to run the optimization we think it would be beneficial to introduce retries into evaluating each 
solution and taking the mean of the metrics. This will provide a more accurate picture of performance and help to 
filter out any flukes in the solutions. 

We would like to introduce more objectives as metrics on the performance of the solutions. Due to the limited time we 
had to work we were not able to implement them in time. 

Expanding the space of the decisions might lead to better optimizations that we were unable to observe. Perhaps 
increasing the population and number of generations to much higher numbers will introduce more optimization at the 
cost of run time. 

Increasing the population size and the max retries of the DE algorithm will allow for more diversity in the solutions 
which could lead to a better solution. Perhaps running this on something other than a desktop machine would help to 
control the significant increase in time.

Finally we think it would be interesting to run a GA using the GA problem in order to optimize itself. Perhaps with 
each retry, introducing the decisions of the best candidate from the previous try to use as the parameters on the 
next run. 


## References
[1] https://github.com/txt/ase16/blob/master/doc/de.md
<br> [2] https://github.com/ase16-ta/ga
