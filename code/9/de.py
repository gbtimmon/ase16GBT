from __future__ import print_function, unicode_literals
from __future__ import division
from DTLZ7 import DTLZ7
from random import random, randint
from Comparator import check_type1, check_type2


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
    frontier = [mode() for _ in range(frontier_size)]
    prev = []
    lives = 5

    # eras
    for k in range(max_tries):
        frontier, cur = update(mode, f, cf, frontier)
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


if __name__ == "__main__":
    de(mode=DTLZ7)
    #d = DTLZ7()
    #print(d.decisionSpace)