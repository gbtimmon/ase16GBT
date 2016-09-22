from __future__ import division, print_function
from sys import float_info, stdout, argv
from math import e
from random import *


# input is a tuple with five dimensions
def f1(s):
    return -(25 * (s.x1 - 2) ** 2 + (s.x2 - 2) ** 2 + ((s.x3 - 1) ** 2) * ((s.x4 - 4) ** 2) + (s.x5 - 1) ** 2)


def f2(s):
    return s.x1 ** 2 + s.x2 ** 2 + s.x3 ** 2 + s.x4 ** 2 + s.x5 ** 2 + s.x6 ** 2


class Solution:
    def __init__(self, x1, x2, x3, x4, x5, x6):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.x6 = x6
        self.f1 = f1(self)
        self.f2 = f2(self)


def score(f1, f2):
    return f1 + f2


def newx():
    x1 = randint(0, 10)
    x2 = randint(0, 10)
    x3 = randint(1, 5)
    x4 = randint(0, 6)
    x5 = randint(1, 5)
    x6 = randint(0, 10)
    return Solution(x1, x2, x3, x4, x5, x6)


def ok(s):
    g1 = 0 <= s.x1 + s.x2 - 2
    g2 = 0 <= 6 - s.x1 - s.x2
    g3 = 0 <= 2 - s.x2 + s.x1
    g4 = 0 <= 2 - s.x1 + 3 * s.x2
    g5 = 0 <= 4 - (s.x3 - 3) ** 2 - s.x4
    g6 = 0 <= (s.x5 - 3) ** 3 + s.x6 - 4
    return g1 and g2 and g3 and g4 and g5 and g6


def new_valid_x():
    while True:
        s = newx()
        if(ok(s)):
            return s


def energy(f1, f2):
    return (((f1 + f2) - min) / float((max - min)))

eb = 0
s = new_valid_x()
max = score(f1(s), f2(s))
min = max
for i in xrange(10**3):
    s = new_valid_x()
    sc = score(f1(s), f2(s))
    if(sc > max):
        max = sc
    if(sc < min):
        min = sc
max_tries = 10**3
max_changes = 10**3
p = 0.5


for i in xrange(max_tries):
    solution = new_valid_x()

    for j in xrange(max_changes):
        if energy(solution.f1, solution.f2) > max:
            sb = solution
            eb = energy(solution.f1, solution.f2)

        c = randint(1, 6)
        if p < random():
            while True:
                if c == 1:
                    solution.x1 = randint(0, 10)
                if c == 2:
                    solution.x2 = randint(0, 10)
                if c == 3:
                    solution.x3 = randint(1, 5)
                if c == 4:
                    solution.x4 = randint(0, 6)
                if c == 5:
                    solution.x5 = randint(1, 5)
                if c == 6:
                    solution.x6 = randint(0, 10)
                if ok(solution):
                    solution.f1 = f1(solution)
                    solution.f2 = f2(solution)
                    en = energy(solution.f1, solution.f2)
                    if(en > eb):
                        eb = en
                        sb = solution
                break
        else:
            while True:
                if c == 1:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x1 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
                if c == 2:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x2 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
                if c == 3:
                    sn = solution
                    for x in xrange(1, 6):
                        sn.x3 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
                if c == 4:
                    sn = solution
                    for x in xrange(1, 7):
                        sn.x4 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
                if c == 5:
                    sn = solution
                    for x in xrange(1, 6):
                        sn.x5 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
                if c == 6:
                    sn = solution
                    for x in xrange(1, 11):
                        sn.x6 = x
                        if ok(sn):
                            solution = sn
                            solution.f1 = f1(s)
                            solution.f2 = f2(s)
                            en = energy(solution.f1, solution.f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                    break
            
print('\n')
print('SB:')
print('X1 = %d', sb.x1)
print('X2 = %d', sb.x2)
print('X3 = %d', sb.x3)
print('X4 = %d', sb.x4)
print('X5 = %d', sb.x5)
print('X6 = %d', sb.x6)
print('F1 = %d', sb.f1)
print('F2 = %d', sb.f2)
print('EB = %f', eb)