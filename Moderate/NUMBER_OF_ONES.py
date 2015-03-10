"""
    Write a program which determines the number of 1 bits in the internal representation of a given integer.
    
    INPUT SAMPLE:
    
    The first argument is a path to a file. The file contains integers, one per line.
    
    For example:
    
    
    1
    2
    3
    10
    22
    56
    OUTPUT SAMPLE:
    
    Print to stdout the number of ones in the binary form of each number.
    
    For example:
    
    
    1
    2
    3
    2
    3
    3


"""

#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")

for line in txt.read().split("\n"):
	if line.isalnum():
		num=int(line)
		num=bin(num)
		length=len(num)
		count=0
		for x in range(2,length):
			if num[x]=="1":
				count+=1
		print count
