from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import random
from sys import stdout, maxint
from math import exp
from DTLZ7 import DTLZ7
from Comparator import check_type1, check_type2

def sa(model, baseline):
    # cooling function
    def probability(en, e, T):
        p = exp((e - en) / (T))
        return p

    # base line study
    def findMinMax():
        s = model()
        max = -maxint - 1
        min = maxint
        for i in xrange(100):
            sn = model()
            curEval = sn.score()
            if curEval > max:
                max = curEval
            elif curEval < min:
                min = curEval
        return (min, max)

    # normalize energy
    def energy(eval, min, max):
        return (eval - min) / (max - min)

    # vars
    min, max = findMinMax()
    s = model()
    s.candidates = baseline.candidates[:]
    sb = model()
    sb.copy(s)
    e = energy(s.score(), min, max)
    eb = e
    kmax = 1000
    linewidth = 50
    stdout.write('\n %4d : %f ,' % (1, eb))
    prev = []
    cur = []
    lives = 5

    # iteration through eras
    for k in xrange(1, kmax):
        T =  k / kmax
        sn = model()
        en = energy(sn.score(), min, max)
        #use type 1 to compare s sn and sb
        if check_type1(sn, sb):
            eb = en
            sb.copy(sn)
            s.copy(sn)
            stdout.write('!')
        elif check_type1(sn, s):
            s.copy(sn)
            e = en
            stdout.write('+')
        elif probability(en, e, T) < random():
            s.copy(sn)
            e = en
            stdout.write('?')
        else:
            stdout.write('.')
        cur.append(en)

        # when reached the end of an era
        if k % linewidth == 0:
            #check type 2
            if not prev:
                prev = cur[:]
            else:
                lives += check_type2(prev,cur)
                prev = cur[:]
            if lives == 0:
                print('\nno changing between eras, terminating program')
                break
            cur = []
            stdout.write('\n %4d : %f ,' % (k, eb))
    print("")
    print("Best solution: %s, " % sb.candidates, "\nf1 and f2: %s, " % sb.score())
    return sb


if __name__ == "__main__":
    sa(DTLZ7)