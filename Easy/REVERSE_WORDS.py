# Reverse Words

"""
    Write a program which reverses the words in an input sentence.
    
    INPUT SAMPLE:
    
    The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.
    
    For example:
    
    
    1
    2
    Hello World
    Hello CodeEval
    OUTPUT SAMPLE:
    
    Print to stdout each sentence with the reversed words in it, one per line. Empty lines in the input should be ignored. Ensure that there are no trailing empty spaces in each line you print.
    
    For example:
    
    
    1
    2
    World Hello
    CodeEval Hello
"""


#imports script, filename

from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")



for line in txt.read().split("\n"):
	#Only performs functions on non-empty lines
	if line!="":
		#Splits the words of a line into a list
		words=line.split()
		
		#Flips the order of the aforementioned words
		words=words[::-1]
		
		#Joins the words in the list back into a string
		words2=" ".join(words)
		
		#Prints the aforementioned strings
		print words2