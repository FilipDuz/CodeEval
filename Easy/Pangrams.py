
"""
The sentence 'A quick brown fox jumps over the lazy dog' contains every single letter in the alphabet. Such sentences are called pangrams. You are to write a program, which takes a sentence, and returns all the letters it is missing (which prevent it from being a pangram). You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order. You should also ignore all non US-ASCII characters.In case the input sentence is already a pangram, print out the string NULL
"""

"""
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. This file will contain several text strings, one per line. E.g.
    
    A quick brown fox jumps over the lazy dog
    A slow yellow fox crawls under the proactive dog
    OUTPUT SAMPLE:
    
    Print out all the letters each string is missing in lowercase, alphabetical order . E.g.
    
    NULL
    bjkmqz
"""

from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")


#Dictionary with individual letters
letters={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,\
"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}


#For loop to convert all letters to lowercase
for line in txt.read().split("\n"):
	#Creates a variable to facilitate counting
	count=0
	
	#Creates dictionary with individual letters
	letters={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,\
"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
	
	#Creates string without whitespace or uppercase letters
	new_sentence=(line.replace(" ","")).lower()
	
	#Strips all non alpha characters
	new_sentence="".join([c for c in new_sentence if c.isalpha()])
	
	#For loop which adds +1 to a letters occurrence count
	for x in range(0,len(new_sentence)):
		letters[new_sentence[x]]+=1
	
	#Creates a list of all letters with an occurrence of zero
	list2=sorted([x for x in letters if letters[x]==0])
	
	#If the above stated list is empty, this implies all letters were used, returning NULL
	#If the above stated list is non empty, the enclosed letters are returned in a string
	if len(list2)==0:
		print "NULL"
	else:
		str1="".join(list2)
		print str1
	
	

