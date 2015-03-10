#FIRST_NON-REPEATED_CHARACTER

#Prints the first character that isn't repeated in a string

from sys import argv
script, filename=argv

#Assigns file object to text
txt=open(filename,"r")

for line in txt.read().split("\n"):
	
	#Only performs loop if line contains text
	if line:
		text1=line
		text2=list(line)

		
		for x in text2:
			if text1.count(x)==1:
				print x
				break
				
txt.close()