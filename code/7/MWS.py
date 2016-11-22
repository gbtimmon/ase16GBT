from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import random, randint
from DTLZ7 import DTLZ7
from Comparator import check_type1, check_type2

def MWS(model):
    #local search
    def localSearch(s, direction):
        sn = model()
        sn.copy(s)
        sLocal = model()
        sLocal.copy(sn)
        eLocal = sLocal.score()
        for val in xrange(int(s.decisions[direction].lo / 100), int(s.decisions[direction].hi / 100)):
            sn.decisions[direction] = val* 100
            if not sn.check():
                continue
            if sn.sum() > eLocal:
                sLocal.copy(sn)
                eLocal = sn.sum()
        return sLocal

    # vars
    maxTries = 25
    maxChanges = 150
    p = 0.5
    sb = model()
    eb = 0
    prev = []
    lives = 5

    # retries
    for tries in xrange(0, maxTries):
        cur = []
        s = model()
        e = s.score()
        if tries == 0:
            sb.copy(s)
            eb = e

        # in each try, search for the best solution
        for changes in xrange(0, maxChanges):
            if p < random():
                s = model()
            else:
                direction = randint(0, s.decisionSpace - 1)
                s = localSearch(s, direction)
            curSore = s.score()
            #type 1 comparison
            if check_type1(s, sb):
                eb = curSore
                sb.copy(s)
            cur.append(eb)

        # early termination
        if not prev:
            prev = cur[:]
        else:
            lives += check_type2(prev, cur)
            prev = cur[:]
        if lives is 0:
            print("\n no changing detected, early terminating program")
            break

        print("Current Best solution: %s, " %sb.candidates,"\nf1 and f2: %s, " %sb.fi(), ", at which eval the best x is found: %s" %eb )


    print("Best solution found: %s, " %sb.candidates,"\nf1 and f2: %s, " %sb.fi(), ", at which eval the best x is found: %s" %eb )

    #return
    return eb


if __name__ == "__main__":
    MWS(DTLZ7)