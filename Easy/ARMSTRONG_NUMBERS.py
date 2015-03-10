#ARMSTRONG NUMBERS

"""
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file has a positive integer. E.g.
    
    
    6
    153
    351
    OUTPUT SAMPLE:
    
    Print out True/False if the number is an Armstrong number or not. E.g.
    
    

    True
    True
    False
"""


#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates loop if the line contains text
	if line:
		
		#Creates a variable with the number as an integer
		num=int(line)
		
		#Creates a list with the digits that make up each number
		nums=list(line)
		
		#This is the number of digits in each number
		length=len(nums)
		
		#Initializes the variable which will hold the products of each number
		sum=0
		for x in nums:
			#Raises each digit to the nth power, where n is the number of digits in each number
			sum+=int(x)**length
		
		#If a number is an Armstrong number, "True" is printed. If not, "False" is printed.
		if sum==num:
			print "True"
		else:
			print "False"

#Closes file object	
txt.close()

