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
    return math.exp((old - new) / float(t))

def newx():
    return random.randint(-100000, 100000)

def neighbor(s):
    neighbor = s
    jump = 20
    while True:
        neighbor.x += random.randint(-1 * jump, jump)
        if(neighbor.x < 100000 and neighbor.x > -100000):
            neighbor.f1 = f1(neighbor.x)
            neighbor.f2 = f2(neighbor.x)
            return neighbor

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
    return (((f1 + f2) - min) / float((max - min)))

emax = 1
kmax = 999
k = 1
x = newx()
s = Solution(x, f1(x), f2(x))
sb = s
e = energy(s.f1, s.f2)
eb = e

sys.stdout.write('\n %4d : %f ,' % (k-1, eb))
while (k <= kmax and e < emax):
    sn = neighbor(s)
    en = energy(sn.f1, sn.f2)
    '''If better than the best'''
    if(en > eb) :
        sb = sn
        eb = en
        s = sn
        e = en
        sys.stdout.write('!')
    '''if new solution is worse than previous one'''
    if(en < e) :
        if(p(e, en, (k/float(kmax))) < random.random()) :
            '''randomly jump'''
            xn = newx()
            s = Solution(xn, f1(xn), f2(xn))
            e = energy(s.f1, s.f2)
            sys.stdout.write('?')
        else:
            s = sn
            e = en
            sys.stdout.write('+')

    sys.stdout.write('.')
    if(k % 50 == 0):
        sys.stdout.write('\n %4d : %f ,' % (k, eb))
    k = k + 1

print('\n')
print('SB:')
print 'X= %d' % sb.x
print 'F1 = %d' % sb.f1
print 'F2 = %d' % sb.f2
print 'EB = %f' % eb






