#SPLIT THE NUMBER

"""
    
    CHALLENGE DESCRIPTION:
    
    You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-". The challenge is to split the number and evaluate it according to this pattern e.g.
    1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line of the file is a test case, containing the number and the pattern separated by a single whitespace. E.g.
    
    
    
    3413289830 a-bcdefghij
    776 a+bc
    12345 a+bcde
    1232 ab+cd
    90602 a+bcde
    
    
    
    OUTPUT SAMPLE:
    
    For each test case print out the result of pattern evaluation. E.g.
    
    

    -413289827
    83
    2346
    44
    611
    Constraints: 
    N is in range [100, 1000000000]
    
    """


#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only performs loop if line contains text
	if line:
		
		#Splits line into two lists
		line2=line.split(" ")
		split1=list(line2[0])
		split2=list(line2[1])
		
		#Performs loop under the condition that the pattern in question has a "-" symbol
		#Splits number into two numbers at index point alluded to in pattern
		#Prints the difference of the two numbers created by the split
		if "-" in split2:
			ind=split2.index("-")
			split11=split1[:ind]
			split12=split1[ind:]
			
			num1=int("".join(split11))
			
			num2=int("".join(split12))
			
			print num1-num2
		
		#Performs loop under the condition that the pattern in questions has a "+" symbol
		#Splits number into two numbers at index point alluded to in pattern
		#Prints the sum of the two numbers created by the split	
		elif "+" in split2:
			ind=split2.index("+")
			split11=split1[:ind]
			split12=split1[ind:]
			
			num1=int("".join(split11))
			
			num2=int("".join(split12))
			
			print num1+num2
		
		

#Closes file object	
txt.close()