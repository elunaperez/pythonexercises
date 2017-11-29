from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

def main():
	number = int(input("Give me a number to check if is a prime number: "))
	if (isPrime(number) == True):
		print ("The number is prime.")
	else:
		print ("The number is not prime.")

main()
