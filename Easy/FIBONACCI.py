# Print the nth Fibonacci number

#Your program should accept a file as its first argument.

#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")

#For loop to read N
for line in txt.read().split("\n"):
	if line.isalnum():
		#Reads Nth Fibonacci number into N
		N=int(line)
	
		#Initializes a list of Fibonacci numbers, with 0 and 1 as the first numbers
		fnumbers=[0,1]
		#Appends Fibonacci numbers as long as N is larger than 1
		if N>1:
			for x in range(2,N+1):
				#Creates Fibonacci numbers
				fnumbers.append(fnumbers[x-1]+fnumbers[x-2])
		
			print fnumbers[N]
		#Prints 0 or 1 if N is less than or equal to 1
		else:
			print fnumbers[N]
