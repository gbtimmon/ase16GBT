# Implementation of NSGA-II

## Abstract

## Introduction
In this section of Homework the goal was to implement our own version of NSGA-II using knowledge from lectures and implement it
using two versions of comparisons: binary domination (bdom) and continuous domination (cdom). We ran the algorithm against some
of the DTLZ equations, models designed to test optimization algorithms.

## NSGA-II Algorithm
The NSGA-II Algorithm is a multi-objective evolutionary algorithm (MOEA) that takes advantage of a fast non-dominated sorting approach<sup>[1]</sup>.
NSGA-II is an improvement to an original NSGA algorithm. NSGA-II uses crowding distance algorithm to find solutions that are densely 
populated around a specific area and works to spread out the solutions across the objective space. 

![NSGA-II Visualization](http://i.imgur.com/VkbVbTi.gif)
### Binary Domination with Cuboid Sorting

### Continuous Dominiation

## DTLZ
In order to test how NSGA-II performs, a problem set must be created. The set must also be flexible in its number of decisions and objectives in order to test different aspects of the optimizer. For such a purpose a test suite called DTLZ was created. DTLZ uses a variety of different functions to create different flexible scenarios to run an optimizer against.<sup>[2]</sup>

### DTLZ 1

![DTLZ 1](http://i.imgur.com/ZFzvySo.png)

### DTLZ 3

![DTLZ 3](http://i.imgur.com/p3i6aut.png)

### DTLZ 5

![DTLZ 5](http://i.imgur.com/4vflqVj.png)

### DTLZ 7

![DTLZ 7](http://i.imgur.com/1kYWjEh.png)

## Results
Across all DTLZ models the scores between binary domination and continuous domination are fairly similar. With 20 retries the differences seem to be negligible. The hypervolume averages below have been normalized by dividing each hypervolume by the number of objectives that were tested as the hypervolume would grow with an increased number of objectives. Even after normalized most of the Hypervolume scores were better for higher number of objectives. 

### DTLZ 1
As seen in the results below, with each increase in objectives the score increases as well, even after normalizing across objectives. For this problem set the number of decisions does not play a significant role in the difference of scores.

![DTLZ 1 Results](http://i.imgur.com/r1ZaDPo.png)

### DTLZ 3
With DTLZ 3 the results are a little more hazy. On average, the higher the number of objectives the better it performs but there were some outliars which did not perform the same. One example is 6 objectives and 40 decisions with cdom which performed much worse than all the other 6 objective runs. 

![DTLZ 3 Results](http://i.imgur.com/hTewiSb.png)

### DTLZ 5
In the DTLZ 5 equation the clear winner for hypervolume scores was using two objectives which outperformed both 4 and 6 objectives for all number of decisions. Both 4 and 6 objectives performed about the same on average. 

![DTLZ 5 Results](http://i.imgur.com/chHsvuW.png)

### DTLZ 7
Performance for DTLZ 7 was very similar across all numbers of objectives and decisions. This may be due to most of the objectives just using on value so there may not be as much variability. 

![DTLZ 7 Results](http://i.imgur.com/qbrxkEJ.png)

## Threats to Validity


## References
[1] http://ieeexplore.ieee.org.prox.lib.ncsu.edu/document/996017/
<br> [2] http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf
