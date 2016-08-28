#!/usr/bin/python
import sys

def test( f, params=None ) :
  try : 
    print("\n\n#Running %s" % f.__name__)

    if params == None :
       f()
    else :
       f(*params)

    print("#Function successful!\n#")
  except :
    print("#Function failed with exception %s" % sys.exc_info()[0])

"""
   EXERCISE 1 
"""

#The first example, in proper order
def in_order_test () : 
  def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

  def repeat_lyrics():
    print_lyrics()
    print_lyrics()

  repeat_lyrics()

#The first example in improper order.
def out_of_order_test () : 

  repeat_lyrics()

  def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

  def repeat_lyrics():
    print_lyrics()
    print_lyrics()

test(in_order_test)
test(out_of_order_test)

"""
   EXERCISE 2
"""

#The first example with a different permutation of order. 
def out_of_order_test2 () : 

  def repeat_lyrics():
    print_lyrics()

  def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

  repeat_lyrics()
       
test(out_of_order_test2)

"""
   EXERCISE 3
"""

def right_justify( s ):
  print ((" " * (70 - len(s))) + s)
  print("0123456789" * 7)
  #return "%70s" % s

test( right_justify, ["cat"])

test( right_justify, ["String 1 String 2 Styring 3"])
test( right_justify, ["String 1 String 2 Styring 3" * 3])
  
"""
   EXERCISE 4
"""

def exercise_4_1() : 
  def print_spam () :
    print("spam")

  def do_twice(f):
    f()
    f()

  do_twice(print_spam)

test(exercise_4_1)

def exercise_4_2(arg) : 

  def print_spam (iarg) :
    print("spam %s" % iarg)

  def do_twice(f, d):
    f(d)
    f(d)

  do_twice(print_spam, arg)

test(exercise_4_2, [4])

def exercise_4_3_and_4_4(arg) : 

  def print_spam (iarg) :
    print(iarg)

  def do_twice(f, d):
    f(d)
    f(d)

  do_twice(print_spam, arg)

test(exercise_4_3_and_4_4, ["Spam"])
 
def exercise_4_5(arg) : 

  def print_spam (iarg) :
    print(iarg)

  def do_twice(f, d):
    f(d)
    f(d)

  def do_four(f, d) :
    do_twice(f,d)
    do_twice(f,d)

  do_four(print_spam, arg)

test(exercise_4_5, ["Spam"])

"""
   EXERCISE 5
"""
def print_row ():
  print "+ - - - -",

def print_end ():
  print "+"

def print_orow():
  print "/        ",

def print_oend():
  print "/"  

def do_twice(f):
  f()
  f()

def print_2row():
  do_twice(print_row)
  print_end()

def print_2orow():
  do_twice(print_orow)
  print_oend()

def do_four(f):
  do_twice(f)
  do_twice(f)

def print_whole_row() :
  print_2row()
  do_four(print_2orow)

def make_22_grid():
   do_twice(print_whole_row)
   print_2row()

test(make_22_grid)

def print_4row():
  do_four(print_row)
  print_end()

def print_4orow():
  do_four(print_orow)
  print_oend()

def print_whole_4row() :
  print_4row()
  do_four(print_4orow)

def make_44_grid():
  do_four(print_whole_4row)
  print_4row()

test(make_44_grid)
