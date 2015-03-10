"""

There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.

INPUT SAMPLE:

The first argument is a path to the input filename containing two comma-delimited strings, one per line. Ignore all empty lines in the input file.

For example:



Hello World,World
Hello CodeEval,CodeEval
San Francisco,San Jose


OUTPUT SAMPLE:

Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.

For example:



1
1
0
"""

#imports script, filename
from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")

#Reads in text from file
for line in txt.read().split("\n"):
	
	#Only executes body if something exists in "line"
	if line:
		#Splits words in line
		line2=line.split(",")
	
		#Assigns first string to string1, and the second string to string2
		string1=line2[0]
		string2=line2[1]
	
	
	
		length1=len(string1)
		length2=len(string2)
	
		#Compares slice from string 1 and compares it to string 2
		compare1=string1[length1-length2:]
	
	
		#If the slice matches the preferred word, 1 is printed. If not, 0 is printed
		if compare1==string2:
			print "1"
		else:
			print "0"
	
txt.close()