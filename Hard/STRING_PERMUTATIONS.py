#STRING PERMUTATIONS

"""
Write a program which prints all the permutations of a string in alphabetical order. 
We consider that digits < upper case letters < lower case letters. The sorting should be 
performed in ascending order.
"""

"""
PROGRAM EXPLANATION:

This program prints permutations of a string in alphabetical order. 

Initial attempts to create a program to sort strings was met with difficulty, 
as the built-in "sorted()" function was unable to sort alphanumeric strings "naturally". 

This program solves that problem by using ASCII characters. 
The program is constructed as follows:

1. The program first creates a list of all permutations of a string. 
2. A list consisting of lists corresponding to ASCII characters in each string is created. 
3. A dictionary is created with the above created list, assigning each list an index number. 
4. The ASCII list is sorted ny number. As it so happens, this sorts the strings in the manner
requested by the problem. 
5. The sorted ASCII list is passed into the dictionary, which passes an index number into
the original list of permutations. This prints the original string permutations in alphabetical 
order. 

"""

#Imports tools to created permutations of strings
from itertools import permutations

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#-----------------------------------------------------------#
#Below are functions to help sort the permutations properly

#Creates list 
def ASCII_NUMS(x):
	ASCII_List=[]
	for y in x:
		ASCII_List.append(ord(y))
	return ASCII_List
		
#Creates a dictionary that associates each ASCII list with an index, which corresponds to 
#the original list of permutations
def get_index(x):
	dictionary={}
	
	i=0
	for y in x:
		dictionary[tuple(y)]=x.index(y)
	return dictionary
	

#This function prints each permutation in order
"""Each list in the ASCII list corresponds to a permutation. This passes the 
sorted ASCII list into the dictionary, which passes corresponding indicies into the original 
list of permutations, thus printing them in order
"""

def print_sorted(i,j,k):
	print_list=[]
	
	for x in k:
		print_list.append(i[j[tuple(x)]])

	return ",".join(print_list)
#-----------------------------------------------------------#



#This for loop is used to read in strings line by line and sort the permutations of each
for line in txt.read().split("\n"):
	
	#Only performs the loop if text exists in the line
	if line:
		
		#Creates list of permutations of each string in the file
		"""The second part of the list comprehension creates a list of permutations, 
		but returns each permutation as a list of characters. 
		The first part of the list comprehension joins these characters into complete
		strings
		"""
		perms = [''.join(p) for p in permutations(line)]
	
		#Creates list with only unique permutations by using set()
		#sorted() is used on the list in order to create consistency between perms and perms2
		perms=sorted(list(set(perms)))
	
		#Creates list of permutations split up by character
		#sorted() is used on the list in order to create consistency between perms and perms2
		perms2=sorted(set(list(permutations(line))))
	
		
		"""For each list of characters in perms2, ASCII_NUMS() creates lists
		corresponding containing the ASCII numbers of each character
		This will make sorting by number and letter much easier
		"""
		ASCII=[ASCII_NUMS(x) for x in perms2]
	
		#Creates dictionary that associates each permutation with its index number
		indicies=get_index(ASCII)
	
		#Sorts the list of ASCII characters
		sortedASCII=sorted(ASCII)
	
		#Prints the permutations in alphabetical order
		print print_sorted(perms,indicies,sortedASCII)

#Closes file	
txt.close()		
