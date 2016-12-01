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

## Threats to Validity

## References
[1] http://ieeexplore.ieee.org.prox.lib.ncsu.edu/document/996017/
<br> [2] http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf
