from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from random import random, seed, randint
from sys import stdout, maxint
from math import exp, fabs
from DTLZ7 import DTLZ7
from Comparator import check_type1, check_type2

def sa(model, baseline):
    # cooling function
    def probability(en, e, T):
        p = exp((e - en) / T)
        # if en < 0: en  = -en
        # if e < 0: e = -e
        # total = max(e, en)
        # p = exp(-(((en-e)/total)/T**3))
        return p

    # base line study


    # normalize energy
    def energy(eval, min, max):
        return (eval - min) / (max - min)

    # vars
    # print(min, max)
    s = model()
    s.candidates = baseline.candidates[:]
    sb = model()
    sb.copy(s)
    e = s.score()
    eb = e
    kmax = 1000
    linewidth = 50
    stdout.write('\n %4d : %f ,' % (1, eb))
    prev = []
    cur = []
    lives = 5

    # iteration through eras
    a = randint(1, 20)
    seed(a)
    for k in xrange(1, kmax):
        T = (k / kmax)
        sn = model()
        en = sn.score()
        #use type 1 to compare s sn and sb
        p = probability(en, e, T)
        q = random()
        if check_type1(sn, sb):
            eb = en
            sb.copy(sn)
            s.copy(sn)
            stdout.write('!')
        elif check_type1(sn, s):
            s.copy(sn)
            e = en
            stdout.write('+')
        elif p < q:
            # print(p, q)
            s.copy(sn)
            e = en
            stdout.write('?')
        else:
            stdout.write('.')
        cur.append(en)

        # when reached the end of an era
        if k % linewidth == 0:
            #check type 2
            if not prev:
                prev = cur[:]
            else:
                lives += check_type2(prev,cur)
                prev = cur[:]
            if lives == 0:
                print('\nno changing between eras, terminating program')
                break
            cur = []
            stdout.write('\n %4d : %f ,' % (k, eb))
    print("")
    print("Best solution: %s, " % sb.candidates, "\nf1 and f2: %s, " % sb.fi(), sb.score())
    return sb


if __name__ == "__main__":
    sa(DTLZ7, DTLZ7())