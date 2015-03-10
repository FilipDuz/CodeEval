#Reverse Groups

"""
    Given a list of numbers and a positive integer k, reverse the elements of the list, k items at a time. If the number of elements is not a multiple of k, then the remaining items in the end should be left as is.
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file contains a list of numbers and the number k, separated by a semicolon. The list of numbers are comma delimited. E.g.
    
    1,2,3,4,5;2
    1,2,3,4,5;3
    
    
    OUTPUT SAMPLE:
    
    Print out the new comma separated list of numbers obtained after reversing. E.g.
    
    2,1,4,3,5
    3,2,1,4,5
"""

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")


for line in txt.read().split("\n"):
	
	#Only performs loop if line contains text
	if line:
		
		#Splits line into two parts
		line2=line.split(";")
		
		#Creates list of numbers to be manipulated
		split1=line2[0]
		split1=split1.split(",")
		
		#Creates variable which holds the number of integers to be reversed at a time
		y=int(line2[1])
		
		#Index of last letter in split2
		length_n=len(split1)
		
		#Initializes variables to be used in string manipulation
		#X will hold the number from which to start string reversal
		#N will hold the number at which to end string reversal
		#new_list will hold the manipulated string as it is being created
		x=0
		new_list=[]
		n=y
		#Loop operates while n, the outer bound for string reversal, is less than the 
		#length of the list of numbers
		#With each loop, the inner and outer bounds for string reversal are incremented by y
		while n<=length_n:
			
			new_list.extend(split1[x:n][::-1])
			
			#If the outerbound +y is greater than the index of the last number, the remaining
			#numbers are added onto the list unreversed, and the loop ends
			
			
			if n+y>(length_n):
				new_list.extend(split1[n:])
				break
			
			
			
			x+=y
			n+=y
	#Prints the edited list as a string, with each character separated by a comma
	print ",".join(new_list)
	
txt.close()
		