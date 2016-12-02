from __future__ import print_function, unicode_literals
from __future__ import division
from random import random, randint
from math import pi, fabs, sin
from DTLZ import DTLZ1
from GA_Problem import *


def populate(problem, size):
    population = []
    # TODO 6: Create a list of points of length 'size'
    for _ in xrange(size):
        point = problem.generate_one()
        problem.evaluate(point)
        population.append(point)
    return population


def update(problem, f, cf, frontier):
    total = 0
    n = 0
    for point in frontier:
        new = extrapolate(frontier, point, f, cf, problem)
        problem.evaluate(new)
        if problem.better(new, point):
            print("+", end="")
            point.decisions = new.decisions
            point.objectives = new.objectives
        else:
            print("-", end="")
        total += problem.score(point)
        n += 1
    return total, n


def trim(val, index, problem):
    return max(problem.decisions[index].low, min(val, problem.decisions[index].high))


def three_others(frontier, avoid):
    def n(max_val):
        return int(random.uniform(0, max_val))

    def a(lst):
        return lst[n(len(lst))]

    def one_other():
        x = avoid
        while x in seen:
            x = a(frontier)
        seen.append(x)
        return x

    seen = [avoid]
    this = one_other()
    that = one_other()
    the_other_thing = one_other()
    return this, that, the_other_thing


def extrapolate(frontier, one, extrapolation_amount, crossover_freq, problem):
    out = one.clone()
    two, three, four = three_others(frontier, one)
    ok = False
    while not ok:
        changed = False
        for d in xrange(len(one.decisions)):
            ran = random.random()
            x, y, z = two.decisions[d], three.decisions[d], four.decisions[d]
            if ran < crossover_freq:
                changed = True
                new = x + extrapolation_amount * (y - z)
                out.decisions[d] = trim(new, d, problem)
        if not changed:
            ran_index = randint(0, len(one.decisions) - 1)
            out.decisions[ran_index] = two.decisions[ran_index]
        problem.evaluate(out)
        ok = problem.ok(out)
    out.objectives = []
    return out

    
def de(mode, max_tries=3, frontier_size=5, f=0.75, cf=0.3, epsilon=0.01):
    prob = GAProblem(mode, 4, 20)
    frontier = populate(prob, frontier_size)
    initial_pop = [point.clone() for point in frontier]
    
    for _ in range(max_tries):
        update(prob, f, cf, frontier)
    return initial_pop, frontier


if __name__ == "__main__":
    initial, final = de(mode=DTLZ1, max_tries=10)
    print(final)

    print("Initial:")
    for i, point in enumerate(initial):
        print("P{0}: {1}".format(i, point.decisions))

    for point in initial:
        say(str(point.objectives[0]) + " ")
    print()

    print("Final")
    for i, point in enumerate(final):
        print("P{0}: {1}".format(i, point.decisions))

    for point in final:
        say(str(point.objectives[0]) + " ")
    print()
