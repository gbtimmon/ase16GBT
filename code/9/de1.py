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
    
def update_1(mod, f, cf, frontier):
    cur = []
    total = 0
    n = 0
    for x in frontier:
        s = x.score()
        new = extrapolate_1(frontier, x, f, cf, mod)
        if (new.score < s):
            print("+", end="")
            s = new.score
            frontier[i].copy(new)
            cur.append(new.score)
        else:
            print(".", end="")
            cur.append(s)
        total += s
        n += 1
    return total,n


def extrapolate_1(frontier, one, f, cf, mod):
    res = mod()
    res.decisions = one.decisions
    two, three, four = threeOthers(frontier, one.id)
    ok = False
    while not ok:
        changed = False
        for d in range(0,len(one.decisions)-1):
            ran = random()
            x, y, z = two.decisions[d], three.decisions[d], four.decisions[d]
            if ran < cf:
                changed = True
                new = x + f * (y - z)
                ans = trim_1(new, d, mod)
                #res.decisions = trim_1(new, d, mod)  # keep in range
        if not changed:
            ran_index = randint(0, len(one) - 1)
            res.candidates[ran_index] = two.candidates[ran_index]
        ok = res.check()
    return res
    
def trim_1(val,index,mode):
    return max(0, min(index,1))


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
    
def de_1(mode, max_tries=100, frontier_size=3, f=0.75, cf=0.3, epsilon=0.01):
    prob = GAProblem(mode, 4, 20)
    frontier = populate(prob, frontier_size)

    
    for k in range(max_tries):
        total,n = update_1(mode,f,cf,frontier)
        if total/n > (1 - epsilon):
            break
    return frontier


if __name__ == "__main__":
    d = de_1(mode=DTLZ1)
    print(d)
    #d = DTLZ7()
    #print(d.decisionSpace)