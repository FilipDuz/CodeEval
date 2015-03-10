#Gronsfeld Cipher

"""

CHALLENGE DESCRIPTION:

You are given a key and an enciphered message. The message was enciphered with the following vocabulary:
    
    !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    Note: The first symbol is space.

Your task is to decipher the message that was enciphered with the Gronsfeld cipher using the given key.

The Gronsfeld cipher is a kind of the Vigenère cipher and is similar to the Caesar cipher. The only difference is that in the Caesar cipher, each character is shifted along by the same number, while in the Gronsfeld cipher, each character has its own number of shifts. It means that the length of key for the Gronsfeld cipher must be the same as the length of the message. But since it is difficult to remember such a key, especially if the message is long, the key of the message is repeated until it has the same length as the message.



The first argument is a file with different test cases (there are possible test cases with spaces at enciphered message). Each test case contains a key and an enciphered message separated by semicolon.
For example:


31415;HYEMYDUMPS
45162;M%muxi%dncpqftiix"
14586214;Uix!&kotvx3
OUTPUT SAMPLE:

Print to stdout a deciphered message.
For example:



EXALTATION
I love challenges!
Test input.
CONSTRAINTS:

To decode a message, use the following alphabet: " !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

Number of test cases is 40."
"""

#Create string with list of characters
#Create dictionary with all characters and their corresponding indices

#Create list with encrypted word
#Create list that matches key to encrypted word

#take letter in encrypted list, put into dictionary to get index, then subtract number in 
#corresponding position in key. 

#with number above, join character at the corresponding index onto a string


#imports script, filename
from sys import argv
script, filename=argv

#Assigns fie object to text
txt=open(filename,"r")

#Inputs enciphered vocabulary, then turns it into a list of characters
string=' !'+'"'+"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
stringlist=list(string)


#For loop to read in lines and perform requested actions
for line in txt.read().split("\n"):
	
	#Splits the line into two parts
	line2=line.split(";")
	
	#Puts the characters in the key into a list
	key=line2[0]
	key2=list(key)
	
	#Puts the characters in the encrypted word into a list
	word=line2[1]
	word2=list(word)
	
	#Adds the key into the variable key3, which will be used to create a key that is equal 
	#in length to the encoded word
	key3=key2
	
	#While loop to create key that matches each letter in encoded word
	#Sets n equal to 0 for use in the following loop
	n=0
	while len(key3)<len(word2):
		
		
		key3.append(key2[n])
		
		n+=1
		
		if n==(len(key2)):
			n=0
	
	"""The following loop takes each letter in the encoded word and finds its corresponding
	index. From this index is subtracted the number in the key which corresponds to the 
	character in question. This represents the index of the new character. """
	
	
	word3=[]
	"""
	The count variable is used to determine how many spaces back the index should be moved 
	in the enciphered alphabet
	"""
	count=0
	for x in word2:
		string_index=stringlist.index(x)
		string_index=string_index-int(key3[count])
		word3.append(stringlist[string_index])
		count+=1
	
	word4="".join(word3)

	print word4
	
txt.close()	
	
	
	
	
	
	
	
	
	