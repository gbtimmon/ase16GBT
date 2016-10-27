from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform, randint, random, seed
from time import time
from sys import stdout, maxint
from math import exp, sin, sqrt

# model objects
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

class Osyczka2(Model):
    def __init__(self):
        self.bottom=[0,0,1,0,1,0]
        self.top=[10,10,5,6,5,10]
        self.decisionSpace=6
        self.decisions=[0,0,0,0,0,0]
        self.any()

    def getObjectives(self):
        f1 = - (25 * (self.decisions[0] - 2)**2 + (self.decisions[1] - 2)**2 + ((self.decisions[2] - 1)**2) * ((self.decisions[3] - 4)**2) + (self.decisions[4] - 1)**2)
        f2 = self.decisions[0] ** 2 + self.decisions[1] ** 2 + self.decisions[2]**2 + self.decisions[3]**2 + self.decisions[4]**2 + self.decisions[5]**2
        return [f1, f2]

    def check(self):
        if self.decisions[0]+self.decisions[1]-2 < 0 or 6-self.decisions[0]-self.decisions[1] < 0 or 2-self.decisions[1]+self.decisions[0] < 0 \
                or 2-self.decisions[0]+3*self.decisions[1] < 0 or 4-self.decisions[3]-(self.decisions[2]-3)**2 < 0 \
                or (self.decisions[4]-3)**3+self.decisions[5]-4 < 0:
            return False
        for i in range(0,self.decisionSpace):
            if self.decisions[i]<self.bottom[i] or self.decisions[i]>self.top[i]:
                return False
        return True

class Kursawe(Model):
    def __init__(self):
        self.bottom=[-5, -5, -5, -5, -5]
        self.top=[5, 5, 5, 5, 5]
        self.decisionSpace=5
        self.decisions=[0, 0, 0, 0, 0]
        self.any()

    def getObjectives(self):
        f1=0
        f2=0
        for i in range(0,self.decisionSpace):
            if i<self.decisionSpace-1:
                f1 += - 10 * exp(-0.2 * sqrt(self.decisions[i]**2 + self.decisions[i + 1]**2))
            f2 += abs(self.decisions[i])**0.8 + 5 * sin(self.decisions[i])
        return [f1,f2]

#utilities
def neighbor(s, model):
    sn = model()
    sn.copy(s)
    while True:
        for index in xrange(s.decisionSpace):
            sn.decisions[index] = uniform(sn.bottom[index], sn.top[index])
        if sn.check():
            break
    return sn

#optimizers
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
            sn = neighbor(s, model)
            # print(sn.decisions)
            curEval = sn.sum()
            # print(curEval)
            if curEval > max:
                max = curEval
            elif curEval < min:
                min = curEval
        return (min, max)

    def energy(eval, min, max):
        return (eval - min) / (max - min)

    min, max = findMinMax()
    # print(min, max)
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





if __name__ == '__main__':
    seed(time())
    # simulated_annealing(Schaffer)
    # simulated_annealing(Osyczka2)
    # simulated_annealing(Kursawe)
    # maxwalksat(Schaffer)
    # maxwalksat(Osyczka2)
    # maxwalksat(Kursawe)
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [simulated_annealing, maxwalksat]:
            print("Optimizer: %s, " %optimizer.__name__,"Model: %s" %model.__name__)
            optimizer(model)
