from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from math import pi, fabs, sin, e
from Model import Model, Decisions, Objectives
from sys import stdout, maxint


class DTLZ7(Model):
    def __init__(self, decisionSpace=10, objectiveSpace=2):
        self.decisions = []
        self.candidates = []
        self.objectives = []
        self.decisionSpace = decisionSpace
        self.objectiveSpace = objectiveSpace
        for i in xrange(self.decisionSpace):
            self.decisions.append(Decisions(0, 1))
        self.objectives.append(Objectives(0, 1))
        self.objectives.append(Objectives(5, 20))
        self.any()
        # self.findMinMax()

    def copy(self, other):
        self.decisions = other.decisions[:]
        self.candidates = other.candidates[:]
        self.decisionSpace = other.decisionSpace
        self.objectiveSpace = other.objectiveSpace

    def score(self):
        # use sum of objectives as score
        res = self.fi()
        val = 0.0
        for i in xrange(self.objectiveSpace - 1):
            val += self.energy(res[i], self.objectives[i].lo, self.objectives[i].hi)
            # print(val)
        return fabs(val/self.objectiveSpace)


    def fm(self, objectives):
        g = 1 + 9 / (self.decisionSpace - self.objectiveSpace + 1) * sum(self.candidates[self.objectiveSpace : ])
        h = self.objectiveSpace
        for x in range(self.objectiveSpace - 1):
            h += (objectives[x] / (1 + g)) * (1 + sin(3 * pi * objectives[x]))

        objectives.append((1 + g) * h)

    def fi(self):
        objectives = []

        # for fis before the last one
        for i in xrange(self.objectiveSpace - 1):
            objectives.append(self.candidates[i])

        # calculate and append the last f
        self.fm(objectives)

        # return
        return objectives

    def cdom(self, other):
        def loss(xl, yl):
            n = len(xl)
            # allloss = [pow((xi-yi)/n,2) for xi,yi in zip(xl,yl)]
            allloss = [-1 * e**(-1 * (xi - yi) / n) for xi,yi in zip(xl,yl)]

            return sum(allloss)/n

        x_objs = self.fi()
        y_objs = other.fi()
        # print(x_objs)
        # print(y_objs)
        l1 = loss(x_objs, y_objs)
        l2 = loss(y_objs, x_objs)
        return l2 - l1

    def findMinMax(self):
        for i in xrange(self.objectiveSpace):
            self.objectives.append(Objectives())

        for i in xrange(1000):
            self.any()
            res = self.fi()
            # print(res)
            for j in xrange(self.objectiveSpace):
                if (self.objectives[j].hi < res[j]):
                    self.objectives[j].hi = res[j]
                if (self.objectives[j].lo > res[j]):
                    self.objectives[j].lo = res[j]

    def energy(self, eval, min, max):
        # print(min, max)
        return (eval - min) / (max - min)


if __name__ == "__main__":
    DTLZ7 = DTLZ7()
    print(DTLZ7.candidates)
    print(DTLZ7.fi())
    DTLZ7.findMinMax()
    print(DTLZ7.score())
    print(DTLZ7.objectives[0].lo,DTLZ7.objectives[0].hi, DTLZ7.objectives[1].lo, DTLZ7.objectives[1].hi)
