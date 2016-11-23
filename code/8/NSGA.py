#%matplotlib inline
# All the imports
from __future__ import print_function, division
#from math import *
import math
import random
import sys
import matplotlib.pyplot as plt

# TODO 1: Enter your unity ID here
__author__ = "magoff2"


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


print("Unity ID: ", __author__)


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
    """
    Represents a member of the population
    """
    def __init__(self, decisions):
        O.__init__(self)
        self.decisions = decisions
        self.objectives = None

    def __hash__(self):
        return hash(tuple(self.decisions))

    def __eq__(self, other):
        return self.decisions == other.decisions

    def clone(self):
        new = Point(self.decisions[:])
        new.objectives = self.objectives[:]
        return new


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

    @staticmethod
    def evaluate(point):
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


class POM3(Problem):
    from pom3.pom3 import pom3 as pom3_helper
    helper = pom3_helper()

    def __init__(self):
        """
        Initialize the POM3 classes
        """
        names = ["Culture", "Criticality", "Criticality Modifier",
                 "Initial Known", "Inter-Dependency", "Dynamism",
                 "Size", "Plan", "Team Size"]
        lows = [0.1, 0.82, 2, 0.40, 1, 1, 0, 0, 1]
        highs = [0.9, 1.20, 10, 0.70, 100, 50, 4, 5, 44]
        # TODO 2: Use names, lows and highs defined above to code up decision
        # and objective metadata for POM3.
        decisions = [Decision(n, l, h) for n, l, h in zip(names, lows, highs)]
        objectives = [Objective("Cost", True, 0, 10000),
                      Objective("Score", False, 0, 1),
                      Objective("Completion", False, 0, 1),
                      Objective("Idle", True, 0, 1)]
        Problem.__init__(self, decisions, objectives)

    @staticmethod
    def evaluate(point):
        if not point.objectives:
            point.objectives = POM3.helper.simulate(point.decisions)
        return point.objectives


pom3 = POM3()
one = pom3.generate_one()
print(POM3.evaluate(one))


def populate(problem, size):
    """
    Create a Point list of length size
    """
    population = []
    for _ in range(size):
        population.append(problem.generate_one())
    return population


def crossover(mom, dad):
    """
    Create a new point which contains decisions from
    the first half of mom and second half of dad
    """
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


def elitism(problem, population, retain_size, dom_func):
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


def ga(pop_size=100, gens=250, dom_func=bdom):
    problem = POM3()
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]
    gen = 0
    while gen < gens:
        say(".")
        children = []
        for _ in range(pop_size):
            mom = random.choice(population)
            dad = random.choice(population)
            while (mom == dad):
                dad = random.choice(population)
            child = mutate(problem, crossover(mom, dad))
            if problem.is_valid(child) and child not in population + children:
                children.append(child)
        population += children
        population = elitism(problem, population, pop_size, dom_func)
        gen += 1
    print("")
    return initial_population, population


def fast_non_dominated_sort(problem, population, dom_func=bdom):
    fronts = []
    for p in population:
        first_front = []
        p.dom_set = []
        p.dom_count = 0
        for q in population:
            if(dom_func(problem, p, q)):
                p.dom_set.append(q)
            elif(dom_func(problem, q, p)):
                p.dom_count += 1
        if(p.dom_count == 0):
            p1.rank = 0
            first_front.append(p)
        fronts.append(first_front)

    curr = 0
    while(curr < len(fronts)):
        next_front = []
        for p1 in fronts[curr]:
            for p2 in p1.dom_set:
                p2.dom_count -= 1
                if(p2.dom_count == 0):
                    p2.rank = curr + 1
                    next_front.append(p2)
        curr += 1
        if(len(next_front) > 0):
            fronts.append(next_front)
    return fronts


def calculate_crowding_distance(problem, population):
    for point in population:
        point.dist = 0.0
    for i in len(problem.objectives):
        min_point =  min(population, key=lambda point: point.objectives[i])
        max_point = max(population, key=lambda point: point.objectives[i])
        rge = max_point.objectives[i] - min_point.objectives[i]
        population[0] = float("inf")
        population[-1] = float("inf")
        if(rge == 0):
            continue
        for j in range(1, len(population) - 1):
            population[j].dist += (population[j+1].objectives[i] - population[j-1].objectives[i]) / rge


def compare(a, b):
    return (a > b) - (a < b)


def crowded_comparison_operator(x, y):
    if(x.rank == y.rank):
        return compare(x.dist, y.dist)
    return compare(x.rank, y.rank)

def nsgaii(pop_size=100, gens=250, dom_func=bdom):
    problem = POM3()
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]



def plot_pareto(initial, final):
    initial_objs = [point.objectives for point in initial]
    final_objs = [point.objectives for point in final]
    initial_x = [i[1] for i in initial_objs]
    initial_y = [i[2] for i in initial_objs]
    final_x = [i[1] for i in final_objs]
    final_y = [i[2] for i in final_objs]
    plt.scatter(initial_x, initial_y, color='b', marker='+', label='initial')
    plt.scatter(final_x, final_y, color='r', marker='o', label='final')
    plt.title("Scatter Plot between initial and final population of GA")
    plt.ylabel("Score")
    plt.xlabel("Completion")
    plt.legend(loc=9, bbox_to_anchor=(0.5, -0.175), ncol=2)
    plt.show()

#initial, final = ga(gens=50)
#plot_pareto(initial, final)

#initial, final = ga(gens=50, dom_func=cdom)
#plot_pareto(initial, final)