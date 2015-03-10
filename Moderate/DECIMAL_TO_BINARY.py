#DECIMAL TO BINARY
#Converts a decimal number into its binary equivalent

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	#Only performs loop if text exists within a line
	if line:
		#Prints binary representation of an integer
		print bin(int(line))[2:]
		
		
	
	

#Closes file object	
txt.close()

