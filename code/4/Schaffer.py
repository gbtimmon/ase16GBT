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
    #return math.exp((old - new) / t)
    return 1

def newx():
    return random.randint(-100000, 100000)

max = schaffer_score(newx())
min = max
for n in xrange(99) :
    x = newx()
    result = schaffer_score(x)
    if(result < min) :
        min = result
    if(result > max) :
        max = result

def energy(f1, f2) :
    return (((f1 + f2) - min) / (max - min))

emax = 1
kmax = 1000
k = 0
x = newx()
s = Solution(x, f1(x), f2(x))
sb = s
e = energy(s.f1, s.f2)
eb = e

print(max)
print(min)
print(s.f1)
print(s.f2)
print(eb)

while (k < kmax and e < emax):
    xn = x + 1
    sn = Solution(xn, f1(xn), f2(xn))
    en = energy(sn.f1, sn.f2)
    '''If better than the best'''
    if(en > eb) :
        sb = sn
        eb = en
        sys.stdout.write('!')
    '''if new solution is worse than previous one'''
    if(en < e) :
        s = sn
        e = en
        sys.stdout.write('+')
    elif(p(e, en, (k/kmax)) < random.random()) :
        '''randomly jump'''
        xn = newx()
        s = Solution(xn, f1(xn), f2(xn))
        e = energy(s.f1, s.f2)
        sys.stdout.write('?')
    sys.stdout.write('.')
    k = k+1
    if(k % 50 == 0):
        sys.stdout.write('\n')






