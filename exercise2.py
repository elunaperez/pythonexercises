num = int(input("Give me a number to divide and know if it's even or odd: "))
check = int(input("Give me a number for dividing the previous number: "))
if ((num % check == 0) and (num % 4 == 0)):
	print ("Our second number divide evenly the first number, the first number it's even and is a multiple of four.")
elif ((num % check == 0) and (num % 2 == 0)):
	print("The second number divide evenly the first number and it's even.")
elif ((num % check == 0) and (num % 2 != 0)): 
	print ("The second number divide evenly the first number and the first number it's odd.")
elif(num % 2 == 0):
	print("The division isn't even yet the first number is even.")
else:
	print("The division isn't even yet the first number is odd.") 