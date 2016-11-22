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

    def score(self, candidates):
        # use sum of objectives as score
        return fabs(sum(self.objs(candidates)))

    def fm(self, candidates, objectives):
        g = 1 + 9 / (self.decisionSpace - self.objectiveSpace + 1) * sum(candidates[self.objectiveSpace - 1:])
        h = self.objectiveSpace
        for x in range(self.objectiveSpace - 1):
            h += (objectives[x] / (1 + g)) * (1 + sin(3 * pi * objectives[x]))

        objectives.append((1 + g) * h)

    def fi(self, candidates):
        objectives = []

        # for fis before the last one
        for i in xrange(self.objectiveSpace - 1):
            objectives.append(candidates[i])

        # calculate and append the last f
        self.fm(candidates, objectives)

        # return
        return objectives

    def objs(self, candidates):
        return self.fi(candidates)


if __name__ == "__main__":
    DTLZ7 = DTLZ7()
    DTLZ7.any()
    print(DTLZ7.candidates)
    print(DTLZ7.fi(DTLZ7.candidates))
    print(DTLZ7.score(DTLZ7.candidates))
