def get_string():
	string = str(input("Give me a string to reverse the word order: "))
	return string

def rWordOrder(string):
	split_string = string.split()
	reverse_string = split_string[::-1]
	reverse_order_string = " ".join(reverse_string)
	return reverse_order_string

print(get_string())

print(rWordOrder(get_string()))