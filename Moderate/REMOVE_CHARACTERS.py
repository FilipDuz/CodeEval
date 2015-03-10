#REMOVE CHARACTERS
"""
    
    Write a program which removes specific characters from a string.
    
    INPUT SAMPLE:
    
    The first argument is a path to a file. The file contains the source strings and the characters that need to be scrubbed. Each source string and characters you need to scrub are delimited by comma.
    
    For example:
    
    
    
    how are you, abc
    hello world, def
    
    
    OUTPUT SAMPLE:
    
    Print to stdout the scrubbed strings, one per line. Ensure that there are no trailing empty spaces on each line you print.
    
    For example:
    
    
    
    how re you
    hllo worl
"""

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Performs loop only if there is text in the line
	if line:
	
		#Splits the file into two parts
		line2=line.split(",")

		#Assigns the string to be edited to string
		string=line2[0]
	
		
		#Creates list of characters to remove from proceeding string
		#Removes unnecessary whitespace
		chars=line2[1]
		chars=chars.strip()
		chars=list(chars)
	
	
	

	
		#Removes selected characters from original string
		for x in chars:
		
			string=string.replace(x,"")
	
		#Prints edited string
		print string
	

	

#Closes file object	
txt.close()