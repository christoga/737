#!/usr/bin/python

def main():
	# City	
	tokyo = 6

	# Input and the times number
	times = 0.375
	input = raw_input("What's the city? ")

	# Input action
	if input == "tokyo":			
		print "The time is ", tokyo * times ,"hour"

if __name__ == '__main__':
	main()