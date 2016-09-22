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
    x1 = random.randint(0, 10)
    x2 = random.randint(0, 10)
    x3 = random.randint(1, 5)
    x4 = random.randint(0, 6)
    x5 = random.randint(1, 5)
    x6 = random.randint(0, 10)
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


s = new_valid_x()
max = score(f1(s), f2(s))
min = max
for i in xrange(10**6):
    s = new_valid_x()
    sc = score(f1(s), f2(s))
    if(sc > max):
        max = sc
    if(sc < min):
        min = sc

max_tries = 10**5
max_changes = 10**5
p = 0.5



for i in xrange(max_tries):
    solution = get_valid_x()

    for j in xrange(max_changes):
        if energy(solution.f1, solution.f2) > max:
            return solution

        c = random.randint(1, 6)
        if p < random.random():
            while True:
                if c == 1:
                    solution.x1 = random.randint(0, 10)
                if c == 2:
                    solution.x2 = random.randint(0, 10)
                if c == 3:
                    solution.x3 = random.randint(1, 5)
                if c == 4:
                    solution.x4 = random.randint(0, 6)
                if c == 5:
                    solution.x5 = random.randint(1, 5)
                if c == 6:
                    solution.x6 = random.randint(0, 10)
                if ok(solution):
                    solution.f1 = f1(solution)
                    solution.f2 = f2(solution)
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
                            en = energy(f1, f2)
                            if(en > eb):
                                eb = en
                                sb = solution
                                break
                if c == 2:
                    solution.x2 = random.randint(0, 10)
                if c == 3:
                    solution.x3 = random.randint(1, 5)
                if c == 4:
                    solution.x4 = random.randint(0, 6)
                if c == 5:
                    solution.x5 = random.randint(1, 5)
                if c == 6:
                    solution.x6 = random.randint(0, 10)
                if ok(solution):
                    solution.f1 = f1(solution)
                    solution.f2 = f2(solution)
                    break

                        if (score(solution) > score(c)):
                res = c
        else:
            maximizeScore(c)
            res = c



class simulated_maxWalkSat() :
    def __init__(
           self,
           metric       = osyczka2,
           output       = True,
           drunk_metric = drunkeness,
           max_iter     = 5000,
           min_energy   = 1e-6,
           valid_range  = (-10e6, 10e6),
           seed         = None,
           bline_iter   = 200
    ):

        self.output     = output
        self.random     = Random()            # seeded random.
        self.metric     = metric              # Function for determining energy
        self.isDrunk    = drunk_metric        # Function for determining if I should go worse
        self.max_iter   = max_iter            # max number of iterations before I give up
        self.min_energy = min_energy          # target energy
        self.range      = valid_range         # valid range of values to search for solution
        self.iter       = 0                   # current iter
        self.terminated = False               # is terminated
        self.omin       = 0
        self.omax       = 0
        self.line_size  = 25

        if( seed is not None ) :
            self.random.seed( int(seed) )

        for _ in xrange( bline_iter ) :
            x = sum( self.metric( self.random.randint( *self.range ) ) )
            self.omin = min( self.omin, x )
            self.omax = max( self.omax, x )

        self.cur_state  = self.random.randint( *self.range ) # initial state
        self.cur_energy = self.energy(self.cur_state)        # initial energy
        self.bst_state  = self.cur_state                     # initial best state
        self.bst_energy = self.cur_energy                    # initial best energy

