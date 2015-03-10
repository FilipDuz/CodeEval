#EVEN NUMBERS
# Program which checks input and determines whether it is even or not


#Your program should accept a file as its first argument.


#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")


for line in txt.read().split("\n"):
	#Only operates on alphanumeric inputs
	if line.isalnum():
		#Converts strings into ints
		numbers=int(line)
		
		#Prints 1 if number is even, and 0 if number is odd
		if numbers%2==0:
			print "1"
		else:
			print "0"