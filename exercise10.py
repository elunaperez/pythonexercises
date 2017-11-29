import random

list_1 = int(input("Give me the length of the first list: \n"))
list_2 = int(input("Give me the length of the second list: \n"))

a = random.sample(range(1,100), list_1)
b = random.sample(range(1,100), list_2)

c = [i for i in a if i in b]
print (c)