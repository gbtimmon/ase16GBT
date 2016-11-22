from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform, randint, random, seed
from time import time
from sys import stdout, maxint
from math import exp, sin, sqrt
from DTLZ7 import DTLZ7

def simulated_annealing(model):
    def probability(en, e, T):
        p = exp((e - en) / (T))
        return p

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

    def energy(eval, min, max):
        return (eval - min) / (max - min)

    min, max = findMinMax()
    s = model()
    sb = model()
    sb.copy(s)
    e = energy(s.score(), min, max)
    eb = e
    kmax = 1000
    linewidth = 50
    stdout.write('\n %4d : %f ,' % (1, eb))
    for k in xrange(1, kmax):
        T =  k / kmax
        sn = model()
        en = energy(sn.score(), min, max)
        if en < eb:
            eb = en
            sb.copy(sn)
            s.copy(sn)
            stdout.write('!')
        elif en < e:
            s.copy(sn)
            e = en
            stdout.write('+')
        elif probability(en, e, T) < random():
            s.copy(sn)
            e = en
            stdout.write('?')
        else:
            stdout.write('.')
        if k % linewidth == 0:
            stdout.write('\n %4d : %f ,' % (k, eb))
    print("")
    print("Best solution: %s, " % sb.candidates, "f1 and f2: %s, " % sb.score(), "steps: %s" % kmax)
    return True


if __name__ == "__main__":
    simulated_annealing(DTLZ7)