#SUM OF DIGITS

"""
    INPUT SAMPLE:
    
    The first argument will be a path to a filename containing positive integers, one per line. E.g.
    
    23
    496
    OUTPUT SAMPLE:
    
    Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.
    
    5
    19
"""

#imports script, filename
from sys import argv
script, filename=argv


#Assigns fie object to text
txt=open(filename,"r")

#For loop to read in lines
for line in txt.read().split("\n"):
	#Only operates if line is alphanumeric
	if line.isalnum():
		
		#Initializes sum variable, which will hold sum of digits
		sum=0
		for x in range(0,len(line)):
			word=""
			
			#Holds individual digits in string format
			word=line[x]
			
			#Adds digit in line to running sum
			sum+=int(word)
		
		#Prints sum	
		print sum
		