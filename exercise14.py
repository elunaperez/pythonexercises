def create_list():
	a = [1, 2, 3, 5, 6, 7, 7, 8, 8, 5, 9, 1] 
	return a

def set_list(a):
	a = set(a)
	return a

print (create_list())
print (set_list(create_list())) 