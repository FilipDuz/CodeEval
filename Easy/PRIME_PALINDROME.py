# Write a program which determines the largest prime palindrome less than 1000.

#Prints numbers between 2 and 1000
numbers=[x for x in range(2,1001)]

#Creates list to hold palindromes
palindromes=[]

#Creates string variable to assist in finding palindromes
string=""

#Creates list to hold prime palindromes
prime_palindrome=[]

#For loop to check if number is a palindrome
for x in numbers:
	string=str(x)
	rstring=string[::-1]
	if string==rstring:
		palindromes.append(int(rstring))

#Checks if palindromes are prime		
for x in palindromes:	
	numbers2=[j for j in range(2,x-1)]
	count=0
	for y in numbers2:
		if x%y==0:
			count+=1
	if count==0:
		prime_palindrome.append(x)

#Prints largest prime

largest=len(prime_palindrome)-1

print prime_palindrome[largest]






