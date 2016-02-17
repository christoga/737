#!/usr/bin/python

def main():
	# City	
	tokyo = 6
	seoul = 5.5
	singapore = 1.5
	angkara = 9
	taipe = 4

	# Input and the times number
	times = 0.375
	input = raw_input("What's the city? ")

	# Input action
	if input == "tokyo":			
		print "The time is ", tokyo * times ,"hour"
	if input == "seoul":			
		print "The time is ", seoul * times ,"hour"
	if input == "singapore":			
		print "The time is ", singapore * times ,"hour"	
	if input == "angkara":			
		print "The time is ", angkara * times ,"hour"
	if input == "taipe":			
		print "The time is ", taipe * times ,"hour"

if __name__ == '__main__':
	main()