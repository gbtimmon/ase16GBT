from __future__ import print_function, division
#from math import *
import math
import random
import sys
import matplotlib.pyplot as plt
from operator import attrgetter


class O:
    """
    Basic Class which
        - Helps dynamic updates
        - Pretty Prints
    """
    def __init__(self, **kwargs):
        self.has().update(**kwargs)

    def has(self):
        return self.__dict__

    def update(self, **kwargs):
        self.has().update(kwargs)
        return self

    def __repr__(self):
        show = [':%s %s' % (k, self.has()[k])
                for k in sorted(self.has().keys())
                if k[0] is not "_"]
        txt = ' '.join(show)
        if len(txt) > 60:
            show = map(lambda x: '\t' + x + '\n', show)
        return '{' + ' '.join(show) + '}'


# Few Utility functions
def say(*lst):
    """
    Print whithout going to new line
    """
    print(*lst, end="")
    sys.stdout.flush()


def random_value(low, high, decimals=2):
    """
    Generate a random number between low and high.
    decimals incidicate number of decimal places
    """
    return round(random.uniform(low, high), decimals)


def gt(a, b):
    return a > b


def lt(a, b):
    return a < b


def shuffle(lst):
    """
    Shuffle a list
    """
    random.shuffle(lst)
    return lst


class Decision(O):
    """
    Class indicating Decision of a problem
    """
    def __init__(self, name, low, high):
        """
        @param name: Name of the decision
        @param low: minimum value
        @param high: maximum value
        """
        O.__init__(self, name=name, low=low, high=high)


class Objective(O):
    """
    Class indicating Objective of a problem
    """
    def __init__(self, name, do_minimize=True, low=0, high=1):
        """
        @param name: Name of the objective
        @param do_minimize: Flag indicating if objective has to be minimized or
        maximized
        """
        O.__init__(self, name=name,
                   do_minimize=do_minimize, low=low, high=high)

    def normalize(self, val):
        return (val - self.low) / (self.high - self.low)


class Point(O):
    id = 0
    """
    Represents a member of the population
    """
    def __init__(self, decisions):
        O.__init__(self)
        self.decisions = decisions
        self.objectives = None
        self.id = Point.id = Point.id + 1

    def __hash__(self):
        return hash(tuple(self.decisions))

    def __eq__(self, other):
        return self.decisions == other.decisions

    def clone(self):
        new = Point(self.decisions[:])
        new.objectives = self.objectives[:]
        return new
        
    def score(self):
        return math.fabs(sum(self.decisions))
        
    def low():
        return max(self.decisions)
        
    def high():
        return min(self.decisions)


class Problem(O):
    """
    Class representing the cone problem.
    """
    def __init__(self, decisions, objectives):
        """
        Initialize Problem.
        :param decisions -  Metadata for Decisions
        :param objectives - Metadata for Objectives
        """
        O.__init__(self)
        self.decisions = decisions
        self.objectives = objectives

    def evaluate(self, point):
        assert False
        return point.objectives

    @staticmethod
    def is_valid(point):
        return True

    def generate_one(self, retries=20):
        for _ in xrange(retries):
            point = Point([random_value(d.low, d.high)
                          for d in self.decisions])
            if self.is_valid(point):
                return point
        raise RuntimeError("Exceeded max runtimes of %d" % 20)


def populate(problem, size):
    """
    Create a Point list of length size
    """
    population = []
    for _ in xrange(size):
        population.append(problem.generate_one())
    return population


def crossover(mom, dad, crossover_rate=1.0):
    """
    Create a new point which contains decisions from
    the first half of mom and second half of dad
    """
    if random.random() > crossover_rate:
        return mom
    n = len(mom.decisions)
    return Point(mom.decisions[:n // 2] + dad.decisions[n // 2:])


def mutate(problem, point, mutation_rate=0.01):
    """
    Iterate through all the decisions in the point
    and if the probability is less than mutation rate
    change the decision(randomly set it between its max and min).
    """
    for i, decision in enumerate(problem.decisions):
        if random.random() < mutation_rate:
            point.decisions[i] = random_value(decision.low, decision.high)
    return point


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


def loss1(problem, i,x,y):
    obj = problem.objectives[i]
    better = lt if obj.do_minimize else gt
    return (x - y) if obj.do_minimize else (y - x)


def expLoss(problem, i,x,y,n):
    return math.exp( loss1(problem, i,x,y) / n)


def loss(problem, one, two):
    objs_one,objs_two = problem.evaluate(one), problem.evaluate(two)
    n      = len(problem.objectives)
    losses = [ expLoss(problem, i,onei,twoi,n)
                 for i, (onei, twoi)
                   in enumerate(zip(objs_one, objs_two)) ]
    return sum(losses) / n


def cdom(problem, one, two):
   "one dominates two if it losses least"
   return loss(problem, one, two) < loss(problem, two, one)


def fitness(problem, population, point, dom_func):
    """
    Evaluate fitness of a point based on the definition in the previous block.
    For example point dominates 5 members of population,
    then fitness of point is 5.
    """
    return len([1 for another in population
                if dom_func(problem, point, another)])


def elitism(problem, population, retain_size, dom_func=bdom):
    """
    Sort the population with respect to the fitness
    of the points and return the top 'retain_size' points of the population
    """
    fitnesses = []
    for point in population:
        fitnesses.append((fitness(problem,
                         population, point, dom_func), point))
    population = [tup[1] for tup in sorted(fitnesses, reverse=True)]
    return population[:retain_size]

