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
