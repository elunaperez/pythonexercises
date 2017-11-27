word = str(input("Give me a word to check if it is a Palindrome:"))

rev_word = word[::-1]

if word == rev_word:
	print ("The word is a palindrome")
else: 
	print ("The word is not a palindrome")

