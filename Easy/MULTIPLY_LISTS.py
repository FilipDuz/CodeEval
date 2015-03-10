#MULTIPLY LISTS

"""
    CHALLENGE DESCRIPTION:
    
    You have 2 lists of positive integers. Write a program which multiplies corresponding elements in these lists.
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Input example is the following
    
    9 0 6 | 15 14 9
    5 | 8
    13 4 15 1 15 5 | 1 4 15 14 8 2
    The lists are separated with a pipe char, numbers are separated with a space char.
    The number of elements in lists are in range [1, 10].
    The number of elements is the same in both lists.
    Each element is a number in range [0, 99].
    
    OUTPUT SAMPLE:
    
    Print the result in the following way.
    
    135 0 54
    40
    13 16 225 14 120 10
"""


#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates loop if lines contain text
	if line:
		
		#Splits line into two lists
		line2=line.split("|")
		
		#Creates a list with only the first half of numbers
		multi1=line2[0]
		multi1=multi1.split()
		
		#Creates a list with only the second half of numbers
		multi2=line2[1]
		multi2=multi2.split()
		
		#Number that corresponds to the amount of numbers in each list
		length=len(multi1)
		
		#Initializes list that will hold the products of the numbers in each list
		product=[]
		for x in range(0,length):
			product.append(int(multi1[x])*int(multi2[x]))
		
		#Converts each integer into a string
		product=map(str,product)
		
		#Prints the products as a string
		print " ".join(product)
			
		
		
		

#Closes file object	
txt.close()