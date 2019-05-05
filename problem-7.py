"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def main():
	number = 1
	for x in range(0, 10001):
		number = next_prime(number)
	print("The 10,001st prime number is {}".format(number))

def next_prime(x=1):
	x+=1
	while not is_prime(x):
		x+=1
	print('Next prime: {}'.format(x))
	return x

def is_prime(number):
	for i in range(2,number):
		if number % i == 0:
			return False
	return True

main()