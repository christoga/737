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
		count("Tokyo", 6)
	elif input == "seoul":
		count("Seoul", 5.5)
	elif input == "singapore":
		count("Singapore", 1.5)
	elif input == "angkara":
		count("Angkara", 4)
	elif input == "taipe":
		count("Taipe", 1.5)
	else:
		print "The city you are looking for is not available"
		main()

def count(name, time):
	'''
	Count the time
	'''
	main = 0.375
	count = time
	print "The time to", name, "is", main * time, "hour"
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
