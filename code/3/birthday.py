#!/usr/bin/python
import sys
import random

def has_duplicates(list) :
  """Returns True if there are duplicate in list, false otherwise"""
  copy = list[:]
  copy.sort()
  for item in range(len(list)-1):
    if copy[item] == copy[item + 1]:
      return True;
  return False;

def gen_birthdays(n):
  """returns a list of random bdays of length n"""
  list = []
  for date in range(n):
    list.append(random.randint(1, 365))
  return list

def num_matches(students, samples):
  """generates sample bdays for number of students and returns count of how many
  had matches"""
  count = 0
  for i in range(samples):
    bday_list = gen_birthdays(students)
    if has_duplicates(bday_list):
      count += 1
  return count

num_students = 23;
num_simulations = 10000
count = num_matches(num_students, num_simulations)

print 'Students: %d' % num_students
print 'Simulations: %d' % num_simulations
print 'Matches: %d' % count

