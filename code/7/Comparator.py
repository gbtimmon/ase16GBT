from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from DTLZ7 import DTLZ7
from stats import a12


def check_type1(X, Y):
    x_list = X.fi()
    y_list = Y.fi()
    for i, (Xi, Yi) in enumerate(zip(x_list, y_list)):
        if Xi >= Yi:
            return False

    return True


'''
 Given a performance measure seen in *m* measures
of *X* and *n* measures of *Y*, the A12 statistics measures the
probability that running algorithm *X* yields higher values than running
another algorithm *Y*. Specifically, it counts how often we seen larger
numbers in *X* than *Y* (and if the same numbers are found in both, we
add a half mark):

     a12= #(X.i > Y.j) / (n*m) + .5#(X.i == Y.j) / (n*m)

According to Vargha and Delaney, a small, medium, large difference
between two populations is:

-   *large* if `a12` is over 71%;
-   *medium* if `a12` is over 64%;
-   *small* if `a12` is 56%, or less.

Here we consider a small effect so we set threshold to 0.56
'''

def check_type2(era, era_1):
    val = a12(era, era_1)
    if val > 0.56:
        return 5
    else:
        return -1


if __name__ == "__main__":
    DTLZ7_1 = DTLZ7()
    DTLZ7 = DTLZ7()
    print('DTLZ7: %s' % DTLZ7.candidates)
    print('DTLZ7_1: %s' % DTLZ7_1.candidates)
    print(check_type1(DTLZ7_1, DTLZ7))
    print(check_type2(DTLZ7_1.candidates, DTLZ7.candidates))
