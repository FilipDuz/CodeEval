#Simple sorting
#sorts floating point numbers


#Imports script and file
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates loop if line contains text
	if line:
		
		#Splits line into list of different numbers
		line=line.split()
		
		#Converts numbers into floats and sorts them
		line=sorted([float(x) for x in line])
	
		#Prints numbers until the third digit after the decimal point
		line=("{0:.3f}".format(x) for x in line)
	
		#Prints each element,separated by a space
		print " ".join(line)

#Closes file	
txt.close()	
	
	
