#BEAUTIFUL STRINGS

"""
    When John was a little kid he didn't have much to do. There was no internet, no Facebook, and no programs to hack on. So he did the only thing he could... he evaluated the beauty of strings in a quest to discover the most beautiful string in the world.
    
    Given a string s, little Johnny defined the beauty of the string as the sum of the beauty of the letters in it. The beauty of each letter is an integer between 1 and 26, inclusive, and no two letters have the same beauty. Johnny doesn't care about whether letters are uppercase or lowercase, so that doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)
    
    You're a student writing a report on the youth of this famous hacker. You found the string that Johnny considered most beautiful. What is the maximum possible beauty of this string?
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file has a sentence. E.g.
    
    
    
    ABbCcc
    Good luck in the Facebook Hacker Cup this year!
    Ignore punctuation, please :)
    Sometimes test cases are hard to make up.
    So I just go consult Professor Dalves
    OUTPUT SAMPLE:
    
    Print out the maximum beauty for the string. E.g.
    
    
    
    152
    754
    491
    729
    646
"""


#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")

#Declare variable to hold string without spaces
strings=""

#For loop to read in each line separately
for line in txt.read().split("\n"):
	#Takes out
	strings=line.replace(" ","")
	strings2=""
	for x in range(0,len(strings)):
		if strings[x].isalpha():
			strings2+=strings[x]
	
	
	strings2=strings2.lower()
	setA=set(strings2)

	listone=[]
	
	
	for x in setA:
		
		listone.append(strings2.count(x))
	listone=sorted(listone)[::-1]
	
	
	
	
	count=26
	sum=0
	for x in range(0,len(listone)):
		sum+=int(listone[x])*count
		count-=1
	print sum
	
		
	

	
		
		
	