from __future__ import division, print_function
from sys import float_info, stdout, argv
from math import e
from random import *


# input is a tuple with five dimensions
def f1(x):
    return -(25 * (x[0] - 2) ** 2 + (x[1] - 2) ** 2 + ((x[2] - 1) ** 2) * ((x[3] - 4) ** 2) + (x[4] - 1) ** 2)


def f2(x):
    return x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2 + x[4] ** 2


def osyczka2(x):
    return (f1(x), f2(x))


def maxWalkSat(tries, changes, threshold, p):
    for i in xrange(tries):
        solution = getx()
        res = solution
        for j in xrange(changes):
            if score(solution) > threshold:
                return solution
            c = mutateX()
            if p < random.random():
                randomC()
                if (score(solution) > score(c)):
                    res = c
            else:
                maximizeScore(c)
                res = c

    return res


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

