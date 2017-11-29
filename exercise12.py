import random

number = int(input("Give me the number for the maximum of the list. \n"))

a = [random.randrange(1,100,1) for i in range(number)]

def first(a):
	return(a[0])

def last(a):
	return(a[len(a) - 1])

def print_list(a):
	"""print("The list is:\n")"""
	for items in a:
		print(items)

'''print_list(a)'''
print ("The first and last element of the list is:")
print (first(a), last(a))