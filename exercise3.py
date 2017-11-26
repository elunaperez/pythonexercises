a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number = int(input("Give me a number to return a list of numbers that is lower than the number:"))

b = []

for i in a:
	if (number >= i):
		b.append(i)

print(b)