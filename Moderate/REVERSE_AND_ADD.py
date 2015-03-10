#REVERSE AND ADD


"""
    The problem is as follows: choose a number, reverse its digits and add it to the original. If the sum is not a palindrome (which means, it is not the same number from left to right and right to left), repeat this procedure.
    
    For example:
    
    195 (initial number) + 591 (reverse of initial number) = 786
    
    786 + 687 = 1473
    
    1473 + 3741 = 5214
    
    5214 + 4125 = 9339 (palindrome)
    In this particular case the palindrome 9339 appeared after the 4th addition. This method leads to palindromes in a few step for almost all of the integers. But there are interesting exceptions. 196 is the first number for which no palindrome has been found. It is not proven though, that there is no such a palindrome.
    
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain an integer n < 10,000. Assume each test case will always have an answer and that it is computable with less than 100 iterations (additions).
    
    OUTPUT SAMPLE:
    
    For each line of input, generate a line of output which is the number of iterations (additions) to compute the palindrome and the resulting palindrome. (they should be on one line and separated by a single space character).
    
    For example:
    
    4 9339
"""

from sys import argv
script, filename=argv



#Assigns file object to text
txt=open(filename,"r")


for line in txt.read().split("\n"):
	#Only performs loop for alphanumeric characters
	#(just in case there is whitespace in the input)
	if line.isalnum():
		
		#Creates two variables; one with the original number, 
		#and one with the original 
		
		test1=int(line)
		test2=int(line[::-1])
		
		#Sum of the aforementioned numbers
		sum=test1+test2
		
		#Initializes count to 1 for following loop
		count=1
		
		#Repeats the operations from above as long as "sum" is not a palindrome
		while str(sum)!=str(sum)[::-1]:
			test1=sum
			test2=int(str(test1)[::-1])
			sum=int(test1+test2)
			count+=1
		
		#Prints the number of iterations required to get a palindrome
		print count,
		
		#Prints the palindrome
		print str(sum)
		

	
	