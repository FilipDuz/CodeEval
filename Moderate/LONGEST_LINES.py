#LONGEST LINES

"""
Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line indicates the number of lines you should output, the other lines are of different length and are presented randomly. You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:


2
Hello World
CodeEval
Quick Fox
A
San Francisco
OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:



San Francisco
Hello World

"""

#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")

#Variable to hold number of strings to be printed
n=0

#Variable to hold lines from file
words=[]

for line in txt.read().split("\n"):
	words.append(line)

#Assigns number of lines to be printed
n=int(words[0])

#Sorts the strings in "words" by their lengths
words.sort(key=len,reverse=True)

#Prints "n" strings
for x in range(0,n):
	print words[x]

