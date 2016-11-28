from __future__ import print_function, unicode_literals
from __future__ import division
from math import pi, fabs, sin
from DTLZ import DTLZ1

def populate(problem, size):
    population = []
    # TODO 6: Create a list of points of length 'size'
    for _ in xrange(size):
    	population.append(problem.generate_one())
    return population
    
def check_type1_1(X, Y):
    return X.score() < Y.score()
    
def update_1(mod, f, cf, frontier):
    cur = []
    for x in enumerate(frontier):
        s = x.score()
        new = extrapolate(frontier, x, f, cf)
        if check_type1_1(new.score, s):
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

def update(mod, f, cf, frontier):
    cur = []
    for i, x in enumerate(frontier):
        s = x.score()
        new = extrapolate(frontier, x.candidates, f, cf, i, mod)
        new_sc = new.score()
        if check_type1(new, x):
            print("+", end="")
            s = new_sc
            frontier[i].copy(new)
            cur.append(new_sc)
        else:
            print(".", end="")
            cur.append(s)
    return frontier, cur


def extrapolate(frontier, one, f, cf, id, mode):
    res = mode()
    res.candidates = one[:]
    two, three, four = threeOthers(frontier, id)
    ok = False
    while not ok:
        changed = False
        for d in range(len(one)):
            ran = random()
            x, y, z = two.candidates[d], three.candidates[d], four.candidates[d]
            if ran < cf:
                changed = True
                new = x + f * (y - z)
                res.candidates[d] = trim(new, d, mode)  # keep in range
        if not changed:
            ran_index = randint(0, len(one) - 1)
            res.candidates[ran_index] = two.candidates[ran_index]
        ok = res.check()
    return res

def extrapolate_1(frontier, one, f, cf, id, mode):
    two, three, four = threeOthers(frontier, id)
    ok = False
    while not ok:
        changed = False
        for d in range(len(one)):
            ran = random()
            x, y, z = two.candidates[d], three.candidates[d], four.candidates[d]
            if ran < cf:
                changed = True
                new = x + f * (y - z)
                res.candidates[d] = trim(new, d, mode)  # keep in range
        if not changed:
            ran_index = randint(0, len(one) - 1)
            res.candidates[ran_index] = two.candidates[ran_index]
        ok = res.check()
    return res

def trim(val,index,mode):
    mod = mode()
    if val > mod.decisions[index].hi:
      val = val % (mod.decisions[index].hi - mod.decisions[index].lo)
    while val < mod.decisions[index].lo:
      val = mod.decisions[index].hi - mod.decisions[index].lo + val
    return val


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

def de(mode, max_tries=100, frontier_size=50, f=0.75, cf=0.3, epsilon=0.01):
    # vars
    ib = 0
    problem_DTLZ = mode()
    frontier = populate(problem_DTLZ, frontier_size)
    #frontier = [mode() for _ in range(frontier_size)]
    prev = []
    lives = 5

    # eras
    for k in range(max_tries):
        frontier, cur = update_1(mode, f, cf, frontier)
        print("Tries: %2d, : current solutions: %s, " % (k, cur), end="\n")
        if not prev:
            prev = cur[:]
        else:
            lives += check_type2(prev, cur)
            prev = cur[:]
        if lives is 0:
            print("\n no changing detected, early terminating program")
            break

    # find best candidate
    ib = 0
    score = None
    for i, x in enumerate(frontier):
        if score is None:
            score = x.score()
        else:
            curScore = x.score()
            if score > curScore:
                score = curScore
                ib = i

    f1, f2 = frontier[ib].fi()
    print(f1, f2, frontier[ib].candidates, score)
    return frontier[ib]
    
def de_1(mode, max_tries=100, frontier_size=50, f=0.75, cf=0.3, epsilon=0.01):
    # vars
    ib = 0
    problem_DTLZ = mode()
    frontier = populate(problem_DTLZ, frontier_size)
    #frontier = [mode() for _ in range(frontier_size)]
    prev = []
    lives = 5
    
    for k in range(max_tries):
        total,n = update_1(mode,f,cf,frontier)
        if total/n > (1 - epsilon):
            break
    return frontier


if __name__ == "__main__":
    de_1(mode=DTLZ1)
    #d = DTLZ7()
    #print(d.decisionSpace)