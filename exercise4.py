x = range (1,100)
divisors = []

number = int(input("Give me a number to return it's divisors:"))

for i in x:
	if ((number % i == 0)):
		divisors.append(i)

print (divisors)