"""
    CARD NUMBER VALIDATION
    CHALLENGE DESCRIPTION:
    
    To check whether a bank card number is valid or it is it just a set of random numbers, Luhn formula is used.
    
    The formula verifies a number against its included check digit, which is usually appended to a partial account number to generate the full account number. This account number must pass the following test:
    
    From the rightmost digit, which is the check digit, moving left, double the value of every second digit; if the product of this doubling operation is greater than 9 (for example, 7×2=14), then sum the digits of the products (for example, 12:1+2=3, 14:1+4=5).
    Take the sum of all the digits.
    If the total modulo 10 is equal to 0 (if the total ends in zero) then, according to the Luhn formula, the number is valid; otherwise, it is not valid.
    Examples of formula calculation and result checking:
    
    Checking number 1556 9144 6285 339
    
    1   5   5   6   9   1   4   4   6   2   8   5   3   3   9
    1   10  5   12  9   2   4   8   6   4   8   10  3   6   9
    1 + 1 + 5 + 3 + 9 + 2 + 4 + 8 + 6 + 4 + 8 + 1 + 3 + 6 + 9 = 70
    
    70 mod 10 = 0, card number is valid
    
    Checking number 6363 1811 2857 7650
    
    6   3   6   3   1   8   1   1   2   8   5   7   7   6   5   0
    12  3   12  3   2   8   2   1   4   8   10  7   14  6   10  0
    3 + 3 + 3 + 3 + 2 + 8 + 2 + 1 + 4 + 8 + 1 + 7 + 5 + 6 + 1 + 0 = 57
    
    57 mod 10 = 7 <> 0, card number is not valid
    
    INPUT SAMPLE:
    
    The first argument is a file that contains bank card numbers, one per line. For better readability, numbers are split into groups of 4 digits separated by spaces.
    
    For example:
    
    
    1
    2
    3
    4
    5
    6011 5940 0319 9511
    5537 0213 6797 6815
    5574 8363 8022 9735
    3044 8507 9391 30
    6370 1675 9034 6211 774
    OUTPUT SAMPLE:
    
    Print to stdout the results of bank card numbers validation, one per line. If the number is correct – print 1, otherwise – print 0.
    
    For example:
    
    
    1
    2
    3
    4
    5
    0
    1
    0
    0
    1
    CONSTRAINTS:
    
    Bank card numbers can be from 12 to 19 digits length.
    Numbers are split into groups of 4 digits separated by spaces, spaces should be ignored.
    Number of test cases is 100.
"""


#imports script, filename
from sys import argv
script, filename=argv



#Assigns fie object to text
txt=open(filename,"r")


for line in txt.read().split("\n"):
	#Creates string variable with whitespace removed
	new_sentence=(line.replace(" ",""))
	
	#Creates reversed string
	new_sentence1=new_sentence[::-1]
	
	#Creates strings for every other number starting from both 0 and 1
	new_sentence11=new_sentence1[::2]
	new_sentence22=new_sentence1[1::2]
	
	#Creates list to hold digits from new_sentence22 multiplied by 2
	new_sentence33=[]
	#Multiplies digits from new_sentence22 by 2
	for x in range(0,len(new_sentence22)):
		holder=(int(new_sentence22[x]))*2

		#Sums the digits of numbers greater than 10, and appends them to new_sentence33
		if holder>=10:
			holder2=str(holder)
			holder3=(int(holder2[0])+int(holder2[1]))
			new_sentence33.append(holder3)
		#Appends all other numbers to new_sentence33
		elif holder<10:
			new_sentence33.append(holder)


#Code for summing edited digits of original number
	sum1=0
	sum2=0
	l_new_sentence11=[]
	for x in new_sentence33:
		sum1+=x
	for x in range(0,len(new_sentence11)):
		sum2+=int(new_sentence11[x])


	#Prints 1 if sum i divisible by 10, prints 0 otherwise. 
	if (sum1+sum2)%10==0:
		print "1"
	else:
		print "0"
	

		
			
	

	
#	print "\n"
	
