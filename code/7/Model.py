from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform

class Decisions:
    def __init__(self,lo,hi):
        self.hi = hi
        self.lo = lo

class Model(object):

    def any(self):
        while True:
            for dec in self.decisons:
                self.candidate.append(uniform(dec.lo, dec.hi))
            if self.check():
                break

    def check(self):
        for i in range(0, self.decisionSpace):
            if self.candidate[i] < self.decisions[i].lo or self.candidate[i] > self.decisions[i].hi:
                return False
        return True
