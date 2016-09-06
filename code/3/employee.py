#!/usr/bin/python
import sys

class Employee:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def __repr__():
		print('Employee Name: %s, Age: %d', name, age)
	
	def __lt__(self, other):
		return self.age < other.age
	
