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
	if input == "seoul":			
		os.system("city/seoul.py")
	if input == "singapore":			
		os.system("city/singapore.py")
	if input == "angkara":			
		os.system("city/angkara.py")
	if input == "taipe":			
		os.system("city/taipe.py")

if __name__ == '__main__':
	main()
