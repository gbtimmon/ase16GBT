from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals
from math import pi, fabs, sin
from Model import Model, Decisions


class DTLZ7(Model):
    def __init__(self, decisionSpace=10, objectiveSpace=2):
        self.decisions = []
        self.candidates = []
        self.decisionSpace = decisionSpace
        self.objectiveSpace = objectiveSpace
        for i in range(self.decisionSpace):
            self.decisions.append(Decisions(0, 1))
        self.any()

    def copy(self, other):
        self.decisions = other.decisions[:]
        self.candidates = other.candidates[:]
        self.decisionSpace = other.decisionSpace
        self.objectiveSpace = other.objectiveSpace

    def score(self):
        # use sum of objectives as score
        return fabs(sum(self.fi()))

    def fm(self, objectives):
        g = 1 + 9 / (self.decisionSpace - self.objectiveSpace + 1) * sum(self.candidates[self.objectiveSpace - 1:])
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



if __name__ == "__main__":
    DTLZ7 = DTLZ7()
    print(DTLZ7.candidates)
    print(DTLZ7.fi())
    print(DTLZ7.score())
