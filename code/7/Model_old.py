from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform


class Model(object):
    def __init__(self):
        self.bottom = [0]
        self.top = [0]
        self.decisionSpace = 0
        self.decisions = [0]
        self.objectiveSpace = 0

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


class DTLZ7(Model):
    def __init__(self):
        self.bottom = [0] * 10
        self.top = [1] * 10
        self.decisionSpace = 10
        self.decisions = [0] * 10
        self.objectiveSpace = 2
        self.any()

    def getobj(self):
        f = []
        g = 1 + 9 / (self.decnum-self.objnum+1) * sum(self.dec[self.objnum-1:])
        h=self.objnum
        for i in xrange(self.objnum-1):
            f.append(self.dec[i])
            h=h-f[i]/(1+g)*(1+np.sin(3*np.pi*f[i]))
        f.append((1+g)*h)
        self.lastdec=self.dec
        self.obj=f
        return f

    def getObjectives(self):
        res = []
        g = 1 + 9 / (self.)
