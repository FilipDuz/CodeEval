#PENULTIMATE WORD
#Prints second to last word from a line of text

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	#Only operates if line contains text
	if line:
		
		#Splits line into list of separate words
		line2=line.split(" ")
	
		#Prints second to last word
		print line2[len(line2)-2]

#Closes file object	
txt.close()