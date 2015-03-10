#Prints out the sum of integers read from a file


#imports script, filename
from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")

total=0
#For loop to add numbers from each line
for line in txt.read().split("\n"):
	#Converts string to integer only if the string is numeric
	if line.isdigit():
		placeholder=int(line)
		total+=int(placeholder)

#Prints sum of integers	
print total
#Closes file object	
txt.close()