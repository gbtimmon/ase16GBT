from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from DTLZ7 import DTLZ7

def check_type1(X, Y):
    x_list = X.fi()
    y_list = Y.fi()
    for i, (Xi, Yi) in enumerate(zip(x_list, y_list)):
        if Xi >= Yi:
            return False

    return True


if __name__ == "__main__":
    DTLZ7_1 = DTLZ7()
    DTLZ7 = DTLZ7()
    print('DTLZ7: %s' %DTLZ7.candidates)
    print('DTLZ7_1: %s' %DTLZ7_1.candidates)
    print(check_type1(DTLZ7_1, DTLZ7))

