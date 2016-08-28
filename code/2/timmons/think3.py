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

def make_border(cols) :
    return (("+ " + ( "- " * 4 )) * cols) + "+\n"

def make_row(cols):
    return ((("/ " + ( "  " * 4 )) * cols) + "+\n") * 4

def print_grid(x,y) :
  print (((make_border(y) + make_row(y)) * x) + make_border(y))

test(print_grid, [2,2])

test(print_grid, [4,4])

