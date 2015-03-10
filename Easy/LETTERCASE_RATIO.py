"""
Your task is to write a program which determines (calculates) the percentage ratio
    of lowercase and uppercase letters.
"""


#imports script, filename
from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")

#for loop used to read individual lines
for line in txt.read().split("\n"):
	lower=0
	upper=0
	y=0
	
	#For loop used to count occurrences of uppercase and lowercase letters. 
	for x in line:
		if line[y].isupper()==True:
			upper+=1
			y+=1
		else:
			lower+=1
			y+=1
	
	#Turns integers into floats
	upper+=float(upper)
	lower+=float(lower)
	
	#Total number of letters
	total=upper+lower
	
	#Creates ratio
	lower_ratio=(lower/total)*100.000
	upper_ratio=(upper/total)*100.000
	
	#Formats ratio
	lower_ratio=format(lower_ratio,'.2f')
	upper_ratio=format(upper_ratio,'.2f')


	#Prints the number of lowercase and uppercase letters on each line
	print "lowercase: ",lower_ratio," uppercase: ",upper_ratio
# Closes txt object
txt.close()


#f = open('somefile.txt','r')
#for line in f.read().split('\n'):
 #   print line
#f.close()