#!/usr/bin/python
import sys

class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __repr__(self):
		return 'Employee Name: %s, Age: %d' % (self.name, self.age)
	
	def __lt__(self, other):
		return self.age < other.age
	
x = Employee('John', 40)
print(x)
y = Employee('Jack', 30)
print(y)

list = [x, y]
print list
list.sort()
print list
