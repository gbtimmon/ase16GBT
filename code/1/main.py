#/usr/bin/python2

import utest
import sys
sys.dont_write_bytecode=true

print "\nLoading and testing Timmons\n\n"
import timmons
utest.oks()

print "\nLoading and testing laurel\n\n"
import laurel
utest.oks()

print "\nLoading and testing wang\n\n"
import wang

utest.oks()

print "\nLoading and testing goff\n\n"
import goff
utest.oks()
