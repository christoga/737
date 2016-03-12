#!/usr/bin/python
import os
__author__ = 'Andre Christoga'

def main():
	'''
	Airplane Time
	'''
	input = raw_input("What's the city? ")

	# Input action
	if input == "tokyo":
		# os.system("city/tokyo.py")
		tokyo()
	elif input == "seoul":
		seoul()
	elif input == "singapore":
		singapore()
	elif input == "angkara":
		angkara()
	elif input == "taipe":
		taipe()
	else:
		print "The city you are looking for is not available"

def tokyo():
	main = 0.375
	count = 6
	print "The time is", count * main ,"hour"

def seoul():
	main = 0.375
	count = 5.5
	print "The time is", count * main ,"hour"

def singapore():
	main = 0.375
	count = 1.5
	print "The time is", count * main ,"hour"

def angkara():
	main = 0.375
	count = 4
	print "The time is", count * main ,"hour"

def taipe():
	main = 0.375
	count = 1.5
	print "The time is", count * main ,"hour"

if __name__ == '__main__':
	main()
