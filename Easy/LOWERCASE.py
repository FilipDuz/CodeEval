#Turn string into lowercase

#Your program should accept a file as its first argument.

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	print line.lower()

#Closes file object	
txt.close()