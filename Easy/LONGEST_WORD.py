#LONGEST WORD

"""
    CHALLENGE DESCRIPTION:
    
    In this challenge you need to find the longest word in a sentence. If the sentence has more than one word of the same length you should pick the first one.
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Input example is the following
    
    
    some line with text
    another line
    Each line has one or more words. Each word is separated by space char.
    
    OUTPUT SAMPLE:
    
    Print the longest word in the following way.
    
    

    some
    another
"""

#imports script, filename
from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#If statement to make sure program is only run on lines with text
	if line:
		#Splits line into a list of individual words
		line2=line.split()
	
		#Sorts the aforementioned list by length(longest to shortest)
		line2.sort(key=len,reverse=True)
	
		#Prints the first word in the list (the longest word)
		print line2[0]

	#Closes file object	
	txt.close()