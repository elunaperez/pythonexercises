
name = input("Give me your name: ")

cont = "yes";
while cont == "yes":
	age = int(input("Give me your age: "))
	year = str((2017-age)+100)
	print(name + " will be 100 years old in the year " + year)
	print()
	more_numbers = input("Do you want to give another age?: ")
	if (more_numbers == "yes" ):
		age = int(input("Give me your age: "))
		year = str((2017-age)+100)
		print(name + " will be 100 years old in the year " + year)
		print()
		more_numbers = input("Do you want to give another age?: ")
	else:
		cont = "no"