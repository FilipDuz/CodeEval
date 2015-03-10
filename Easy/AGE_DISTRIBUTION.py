"""
    AGE DISTRIBUTION
    CHALLENGE DESCRIPTION:
    
    You're responsible for providing a demographic report for your local school district based on age. To do this, you're going determine which 'category' each person fits into based on their age.
    The person's age will determine which category they should be in:
    
    If they're from 0 to 2 the child should be with parents print : 'Still in Mama's arms'
    If they're 3 or 4 and should be in preschool print : 'Preschool Maniac'
    If they're from 5 to 11 and should be in elementary school print : 'Elementary school'
    From 12 to 14: 'Middle school'
    From 15 to 18: 'High school'
    From 19 to 22: 'College'
    From 23 to 65: 'Working for the man'
    From 66 to 100: 'The Golden Years'
    If the age of the person less than 0 or more than 100 - it might be an alien - print: "This program is for humans"
    INPUT SAMPLE:
    
    Your program should accept as its first argument a path to a filename. Each line of input contains one integer - age of the person:
    
    
    1
    2
    0
    19
    OUTPUT SAMPLE:
    
    For each line of input print out where the person is:
    
    
    1
    2
    Still in Mama's arms
    College
"""

from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")


numbers=[]
numbers2=[]
#For loop to convert all letters to lowercase
count=0

for line in txt.read().split("\n"):
	numbers.append(line)



for x in range(0,len(numbers)):
	if numbers[x].isalnum() or numbers[x].startswith("-"):
		numbers2.append(int(numbers[x]))



for x in numbers2:		
	
	if 2>=x>=0:
		print "Still in Mama's arms"
	elif 4>=x>=3:
		print "Preschool Maniac"
	elif 11>=x>=5:
		print "Elementary school"
	elif 14>=x>=12:
		print "Middle school"
	elif 18>=x>=15:
		print "High school"
	elif 22>=x>=19:
		print "College"
	elif 65>=x>=23:
		print "Working for the man"
	elif 100>=x>=66:
		print "The Golden Years"
	elif x>100:
		print "This program is for humans"
	elif x<0:
		print "This program is for humans"