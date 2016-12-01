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
        s = problem.score(point)
        new = extrapolate(frontier, point, f, cf, problem)
        if problem.score(new) < problem.score(point):
            print("+", end="")
            s = problem.score(new)
            frontier.copy(new)
        else:
            print(".", end="")
        total += s
        n += 1
    return total, n


def trim(val, index, problem):
    return max(problem.decisions[index].low, min(val, problem.decisions[index].high))


def threeOthers(frontier, avoid):
    def oneOther(seen, selected):
        pick_index = randint(0, len(frontier) - 1)
        if pick_index not in seen:
            seen.append(pick_index)
            selected.append(frontier[pick_index])
    # vars
    seen = []
    seen.append(avoid)
    i = 0
    selected = []

    #find three other objs in frontier
    while len(selected) < 3:
        oneOther(seen, selected)
    return selected[0], selected[1], selected[2]


def extrapolate(frontier, one, extrapolation_amount, crossover_freq, problem):
    out = one.clone()
    two, three, four = threeOthers(frontier, one.id)
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
    return out

    
def de(mode, max_tries=3, frontier_size=5, f=0.75, cf=0.3, epsilon=0.01):
    prob = GAProblem(mode, 4, 20)
    frontier = populate(prob, frontier_size)
    
    for k in range(max_tries):
        total, n = update(prob,f,cf,frontier)
        if total/n > (1 - epsilon):
            break
    return frontier


if __name__ == "__main__":
    d = de(mode=DTLZ1)
    print(d)
    #d = DTLZ7()
    #print(d.decisionSpace)