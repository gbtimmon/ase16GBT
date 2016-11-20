from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform, randint, random, seed
from time import time
from sys import stdout, maxint
from math import exp, sin, sqrt
from Model import Model



def neighbor(s, model):
    sn = model()
    sn.copy(s)
    while True:
        for index in xrange(s.decisionSpace):
            sn.decisions[index] = uniform(sn.bottom[index], sn.top[index])
        if sn.check():
            break
    return sn


def simulated_annealing(model):
    def probability(en, e, T):
        p = exp(-(en - e) / (T))
        return p

    def findMinMax():
        s = model()
        max = s.sum()
        min = max
        for i in xrange(100):
            sn = neighbor(s, model)
            curEval = sn.sum()
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
    e = energy(s.sum(), min, max)
    eb = e
    kmax = 1000
    linewidth = 50
    stdout.write('\n %4d : %f ,' % (1, eb))
    for k in xrange(1, kmax):
        T =  k / kmax
        sn = neighbor(s, model)
        en = energy(sn.sum(), min, max)
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
    print("Best solution: %s, " % sb.decisions, "f1 and f2: %s, " % sb.getObjectives(), "steps: %s" % kmax)
    return True


def maxwalksat(model):
    def localSearch(s, direction):
        sn = model()
        sn.copy(s)
        sLocal = model()
        sLocal.copy(sn)
        eLocal = sLocal.sum()
        for val in xrange(int(s.bottom[direction] / 100), int(s.top[direction] / 100)):
            sn.decisions[direction] = val* 100
            if not sn.check():
                continue
            if sn.sum() > eLocal:
                sLocal.copy(sn)
                eLocal = sn.sum()
        return sLocal

    maxTries = 15
    maxChanges = 100
    p = 0.5
    sb = model()
    eb = 0
    for tries in xrange(0, maxTries):
        s = model()
        e = s.sum()
        if tries == 0:
            sb.copy(s)
            eb = e
        for changes in xrange(0, maxChanges):
            if p < random():
                s = neighbor(s, model)
            else:
                direction = randint(0, s.decisionSpace - 1)
                s = localSearch(s, direction)
            curSum = s.sum()
            if curSum < eb:
                eb = curSum
                sb.copy(s)
        print("Current Best solution: %s, " %sb.decisions,"\nf1 and f2: %s, " %sb.getObjectives(), ", at which eval the best x is found: %s" %eb )
    print("Best solution found: %s, " %sb.decisions,"\nf1 and f2: %s, " %sb.getObjectives(), ", at which eval the best x is found: %s" %eb )



