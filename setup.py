#!/usr/bin/python

def main():
	# City	
	cm = 0.375
	input = raw_input("What's the city? ")

	# Input action
	if input == "tokyo":
		tokyo = 6	
		print "The time is ", tokyo * cm

if __name__ == '__main__':
	main()