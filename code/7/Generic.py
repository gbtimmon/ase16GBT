from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform, randint, random, seed
from time import time
import numpy as np
from sys import stdout
from math import exp
from pdb import set_trace


class Model(object):
    def __init__(self):
        self.bottom = [0]
        self.top = [0]
        self.decisionSpace = 0
        self.decisions = [0]

    def any(self):
        while True:
            for i in range(0, self.decisionSpace):
                self.decisions[i] = uniform(self.bottom[i], self.top[i])
            if self.check():
                break

    def sum(self):
        return sum(self.getObjectives())

    def copy(self, other):
        self.decisions = other.decisions[:]
        self.bottom = other.bottom[:]
        self.top = other.top[:]
        self.decisionSpace = other.decisionSpace

    def getObjectives(self):
        return []

    def check(self):
        for i in range(0, self.decisionSpace):
            if self.decisions[i] < self.bottom[i] or self.decisions[i] > self.top[i]:
                return False
        return True



class Schaffer(Model):
    def __init__(self):
        self.bottom = [-10 ** 5]
        self.top = [10 ** 5]
        self.decisionSpace = 1
        self.decisions = [0]
        self.any()

    def getObjectives(self):
        f1 = self.decisions[0] ** 2
        f2 = (self.decisions[0] - 2) ** 2
        return [f1, f2]


def neighbor(s, index, model):
    sn = model()
    sn.copy(s)
    while True:
        sn.decisions[index] = uniform(sn.bottom[index], sn.top[index])
        if sn.check(): break
    return sn


def simulated_annealing(model):
    def probability(en, e, T):
        p = exp(-(en - e) / (T))
        # print(en, e, T, p)
        return p

    def findMinMax():
        s = model()
        max = s.sum()
        min = max
        for i in xrange(100):
            sn = neighbor(s, randint(0, s.decisionSpace - 1), model)
            curEval = sn.sum()
            if curEval > max:
                max = curEval
            else:
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
    for k in range(1, kmax):
        T =  k / kmax
        sn = neighbor(s, randint(0, s.decisionSpace - 1), model)
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


if __name__ == '__main__':
    seed(time())
    simulated_annealing(Schaffer)
