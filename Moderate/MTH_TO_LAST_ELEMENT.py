"""
    Write a program which determines the Mth to the last element in a list.
    
    INPUT SAMPLE:
    
    The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.
    
    For example:
    
    
    
    a b c d 4
    e f g h 2
    
    
    
    OUTPUT SAMPLE:
    
    Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.
    
    For example:
    
    

    a
    g
"""

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines
for line in txt.read().split("\n"):
	#If statement accounts for the appearance of whitespace
	if line:
		#Splits line into separate characters
		line2=line.split(" ")
	
		#Assigns the number at the end of each line to "n"
		x=len(line2)
		n=int(line2[x-1])
	
		#Prints the letter at the specified index so long as n is less than the number of 
		#characters in the line
	
		if n<=len(line2)-1:
			print line2[-(n+1)]
		
	
