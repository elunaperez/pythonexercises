import random

random.seed()
x = [ (random.randrange(1,100,1)) for i in range(100)]
random.seed()
y = [ (random.randrange(1,100,1)) for i in range(100)]

z = []

for i in x:
	if ((y[i] == x[i])):
		z.append(i)

print(z)