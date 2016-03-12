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
		os.system("city/tokyo.py")
	elif input == "seoul":
		os.system("city/seoul.py")
	elif input == "singapore":
		os.system("city/singapore.py")
	elif input == "angkara":
		os.system("city/angkara.py")
	elif input == "taipe":
		os.system("city/taipe.py")
	else:
		print "The city you are looking for is not available"	

if __name__ == '__main__':
	main()
