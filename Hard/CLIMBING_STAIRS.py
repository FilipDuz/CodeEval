#CLIMBING STAIRS


"""
    You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file contains a positive integer which is the total number of stairs.
    Ignore all empty lines. E.g.
    
    
    10
    20
    OUTPUT SAMPLE:
    
    Print out the number of ways to climb to the top of the staircase. E.g.
    
    
    
    89
    10946
    Constraints: 
    The total number of stairs is <= 1000
    """


# To enable use of factorial function
import math

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")


#Reads in lines
for line in txt.read().split("\n"):
	
	#Prevents unintentional whitespace from causing errors
	if line.isalnum():
		#Assigns number on line to n
		n=int(line)
	
		#To be used in counting the number of 1 steps
		x=n
	
		#To be used in counting the number of 2 steps
		y=0
	
		#Holds the number of ways to ascend stair case given number of 2 and 1 steps
		sum=0
	
	
		#For each iteration, the number of 1 steps decreases by 2, and the number of 2 steps 
		#increase by 1 to compensate
	
		#If n is even, stops loop when x is equal to zero (ascending stairs with only 2 steps)
	
		if x%2==0:
			while x>=0:
				sum+=math.factorial(n)/(math.factorial(x)*math.factorial(y))
				n-=1
				x-=2
				y+=1
		#For each iteration, the number of 1 steps decreases by 2, and the number of 2 steps 
		#increase by 1 to compensate
	
		#If n is odd, stops loop when x is equal to 1 (one 1 step, "y" 2 steps)
		elif x%2!=0:
			while x>=1:
				sum+=math.factorial(n)/(math.factorial(x)*math.factorial(y))
				n-=1
				x-=2
				y+=1
			
		#Prints sum
		print sum

#Notes
"""You are climbing a stair case. It takes n steps to reach to the top. Each time you can
    either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"""


"""The stairs can be climbed in n!/x!y! ways, where n is equal to the number of stairs,
    x is equal to the number of 1 steps, and y is equal to the number of 2 steps"""
