#Roller Coaster
"""
    You are given a piece of text. Your job is to write a program that sets the case of text characters according to the following rules:
    
    The first letter of the line should be in uppercase.
    The next letter should be in lowercase.
    The next letter should be in uppercase, and so on.
    Any characters, except for the letters, are ignored during determination of letter case.
    INPUT SAMPLE:
    
    The first argument will be a path to a filename containing sentences, one per line. You can assume that all characters are from the English language.
    
    For example:
    

    
    To be, or not to be: that is the question.
    Whether 'tis nobler in the mind to suffer.
    The slings and arrows of outrageous fortune.
    Or to take arms against a sea of troubles.
    And by opposing end them, to die: to sleep.
    
    
    OUTPUT SAMPLE:
    
    Print to stdout the RoLlErCoAsTeR case version of the string.
    
    For example:
    
    
    
    To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.
    WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR.
    ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE.
    Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS.
    AnD bY oPpOsInG eNd ThEm, To DiE: tO sLeEp.
    
    CONSTRAINTS:
    
    The length of each piece of text does not exceed 1000 characters.
"""

#Imports script and file
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates loop if line contains text
	if line:
		
		#Splits the text in each line into a list of individual characters
		letters=list(line)
		
		"""
		This loop increments the variable "count". 
		For letters in "letters", when "count" is even, characters are capitalized. 
		When "count" is odd, characters are lowercased.
		
		This loop ignores non-letter characters.
		"""
		count=0
		letters2=[]
		for x in letters:
			if x.isalpha():
				if count%2==0:
					letters2.append(x.upper())
					count+=1
				elif count%2!=0:
					letters2.append(x.lower())
					count+=1
			else:
				letters2.append(x)	
			
	#Joins the individual letters in "letters2" into a single string
	print "".join(letters2)

txt.close()