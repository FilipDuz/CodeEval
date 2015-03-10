#COUNTING PRIMES

"""
    Given two integers N and M, count the number of prime numbers between N and M (both inclusive)
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.
    
    
    2,10
    20,30
    
    
    
    OUTPUT SAMPLE:
    
    Print out the number of primes between N and M (both inclusive)
    
    
    
    4
    2
"""

from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")


#Creates a function that determines whether or not a number is prime
def prime(p):
	#Variable which counts the number of prime numbers
	count=0
	
	#If p is equal to "0", the function returns 0 (as "0" is not prime)
	if p==0:
		return 0
	
	#If p is equal to "1", the function returns 0 (as "1" is not prime)
	elif p==1:
		return 0
	
	#Loop counts the number of times p is divisible by numbers between 2 and p. 
	div_count=0
	for x in range(1,p+1):
		if p%x==0:
			div_count+=1
	
	#If p was not divisible by any number in the range (2,p), this means that it is prime. 
	if div_count==2:
		count+=1
	return count
	

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only performs loop if line contains text
	if line:
		line2=line.split(",")
		
		#Converts the numbers in each line into integers
		n=int(line2[0])
		m=int(line2[1])
		
		
		#Counts the number of prime numbers within the range (n,m)
		count2=0
		for x in range(n,m+1):
			count2+=prime(x)
			

		#Prints the number of prime number with the range (n,m)
		print count2
	

#Closes file object	
txt.close()