#WORD TO DIGIT
#This program reads the names of numbers and prints their integer equivalents

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#Creates dictionary with names of numbers matched to their integer equivalents

d={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7",\
"eight":"8","nine":"9"}

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates loop if line has text
	if line:
		
		#Splits the line into a list of strings
		line2=line.split(";")
		
		#Initializes string variable to hold digits in following loop
		string=""
		for x in line2:
			#Appends the integer corresponding to each number in line2
			string+=d[x]
		
		#Prints the number
		print string

#Closes file object	
txt.close()