from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform


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