import random
	
magic_number = random.randrange(1,10,1)
cont = 0

play = input("Wanna guess the number? (yes/no) ")
if (play == 'no'):
	print("The times you try where: " + str(cont))
else:
	while (play != 'exit'):
		guess = int(input("Give me a number:"))
		if (guess > magic_number):
			cont += 1
			print ("Your number is too high.") 	
			print("Wanna keep guessing the number? ")
			play = input("Yes to continue or exit to leave:\n")
			if (play == 'exit'):
				print("The times you try where: " + str(cont))
		elif (guess < magic_number):
			cont += 1
			print("Your number is too low.")
			print("Wanna keep guessing the number? ")
			play = input("Yes to continue or exit to leave:\n")
			if (play == 'exit'):
				print("The times you try where: " + str(cont))
		elif (guess == magic_number):
			cont += 1
			print("You guess the number.\n")
			print("The times you try where: " + str(cont))
			break