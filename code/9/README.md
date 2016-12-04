### Optimizing the Optimizer

## Abstract

## Introduction
In this part of the homework the goal was to optimize the defaults of the Genetic Algorithm (GA) by running it through an instance of differential evolution. We hypothesize that by tuning the GA it will perform better against an untuned version of the GA with the usual defaults. 

## DE
Differential Evolution is a multi objective optimizer. It optimizes a problem by maintaining a population of candidate solutions and improving it. In order to optimize problems, DE treats the problem as a black box and uses the quality measurements provided by the problem itself to determine whether a solution is better than a previous solution<sup>[1]</sup>. 

## GA

For this problem we used the Genetic Algorithm provided in the code workshop as our basis of the problem. We configured a Problem to take on a GA. The decisions we optimized for were mutation rate, crossover rate, population size and number of generations.

For mutation rate we decided on a range between 0.01 and 0.1. We decided to keep the mutation rate somewhat lower so it wouldn't be mutating the entire population and throwing away any progress towards an ideal solution. We varied the crossover rate between 0.1 and 1.0. We felt that any range of crossover could produce different kinds of results. If we had a slowly changing population it might choose other factors to optimize for. 

For population size we went with a range between 20 and 200. We wanted the population to have a large enough size to effectively crossover between, but we also wanted to keep it under 200 to help limit the runtime for the problem. Finally we decided on a range of 10 and 250 for the number of generations. We were curious to see if limiting the number of generations would have an effect on how well the solutions would perform but we also didn't want to use too many generations in the interest of limiting runtime. 

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
The snippet of code above is the evaluation method of the GA Problem. Each point will be evaluated by running the optimizer with the selected decisions and the results were scored using Hypervolume of the solution. The issue with running a new GA with every candidate solution was the time constraint. When the problem expanded the runtime inflated significantly so we had to be careful to use measures to limit the runtime.

## Results
![Running DE on GA Results](http://i.imgur.com/apjE5X2.png)

## Threats to Validity

## Future Work

## References
[1] https://github.com/txt/ase16/blob/master/doc/de.md
