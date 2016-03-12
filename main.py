#!/usr/bin/python
import time
__author__ = 'Andre Christoga'

def main():
	'''
	Airplane Time
	'''
	input = raw_input("What's the city? ")

	# Input action
	if input == "tokyo":
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
	'''
	Tokyo city
	'''
	main = 0.375
	count = 6
	print "The time is", count * main ,"hour"
	exit()

def seoul():
	'''
	Seoul city
	'''
	main = 0.375
	count = 5.5
	print "The time is", count * main ,"hour"
	exit()

def singapore():
	'''
	Singapore nation
	'''
	main = 0.375
	count = 1.5
	print "The time is", count * main ,"hour"
	exit()

def angkara():
	'''
	Angkara city
	'''
	main = 0.375
	count = 4
	print "The time is", count * main ,"hour"
	exit()

def taipe():
	'''
	Taipei city
	'''
	main = 0.375
	count = 1.5
	print "The time is", count * main ,"hour"
	exit()

def exit():
    input = raw_input("Exit? Yes[y] or No[n] ")
    if input == 'y':
        print 'Exiting program...'
        time.sleep(2)
    elif input == 'n':
        main()
    else:
        print 'Please answer the question'
        exit()

if __name__ == '__main__':
	main()
