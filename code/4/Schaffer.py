#!/usr/bin/python

import random
import sys
import math

class Solution :
    def __init__(self, x, f1, f2):
        self.x = x
        self.f1 = f1
        self.f2 = f2

def f1(x):
    return x * x

def f2(x):
    return (x-2)*(x-2)

def schaffer_score(x) :
    return f1(x) + f2(x)

def p(old, new, t):
    return math.exp((old - new) / t)

max = schaffer_score(random.randint(0, 100000))
min = max
for n in xrange(99) :
    x = random.randint(0, 100000)
    result = schaffer_score(x)
    if(result < min) :
        min = result
    if(result > max) :
        max = result

def energy(f1, f2) :
    return ((f1 + f2) - min) / (max - min)

emax = 1
kmax = 1000
k = 0
x = random.randint(0, 100000)
s = Solution(x, f1(x), f2(x))
sb = s
e = energy(s.f1, s.f2)
eb = e

print(eb)

while (k < kmax and e < emax):
    xn = x + 1
    sn = Solution(xn, f1(xn), f2(xn))
    en = energy(sn.f1, sn.f2)
    if(en > eb) :
        sb = sn
        sys.stdout.write('!')
    if(en < e) :
        s = sn
        e = en
        sys.stdout.write('+')
    elif(p < random.random()) :
        xn = random.randint(0, 100000)
        s = Solution(xn, f1(xn), f2(xn))
        e = energy(s.f1, s.f2)
        sys.stdout.write('?')
    sys.stdout.write('.')
    k = k+1
    if(k % 50 == 0):
        print('\n')






