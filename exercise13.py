def fibonacci():
	fnumber = int(input("Give me the number to know the fibonacci sequence: \n"))
	result = []
	a, b = 0,1
	if (fnumber == 1):
		result.append(1)
		print (result)
	else:
		while b < fnumber:
			result.append(b)
			a,b = b, a+b
		return result

print (fibonacci())
