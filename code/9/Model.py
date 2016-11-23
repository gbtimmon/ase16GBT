from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import uniform
import sys

class Decisions:
    def __init__(self,lo,hi):
        self.hi = hi
        self.lo = lo

class Model(object):
    def any(self):
        while True:
            for dec in self.decisions:
                self.candidates.append(uniform(dec.lo, dec.hi))
            if self.check():
                break

    def check(self):
        for i in range(0, len(self.decisions)):
            if self.candidates[i] < self.decisions[i].lo or self.candidates[i] > self.decisions[i].hi:
                return False
        return True

# sys.path.remove('C:\\Users\\MoonM\\AutomaticSE\\ase16GBT\\code\\7\\Model')
if __name__ == "__main__":
    print(sys.path)