# SET INTERSECTION
#This program prints the intersection of two sets

#imports script, filename
from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Only operates if lines contain text
	if line:
		
		#Splits line into two sets
		line2=line.split(";")
		
		#Creates a set with first portion of line
		set1=line2[0].split(",")
		set1=set(set1)
		
		#Creates a set with second portion of line
		set2=line2[1].split(",")
		set2=set(set2)
		
		#Creates a set with the intersection of the above two sets
		intersect= set1 & set2
		
		#Creates a list with the elements of the intersection
		inter_list=list(intersect)
		
		#Sorts the aforementioned list
		inter_list=sorted(inter_list)
		
		#Prints the aforementioned list, with commas separating individual elements
		print ",".join(inter_list)
			
		
#Closes file object	
txt.close()