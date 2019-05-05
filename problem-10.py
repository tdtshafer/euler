"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def main():
	total = 0
	prime = 2
	while prime < 2e6:
		total += prime
		prime = next_prime(prime)
	print("The sum of primes below 2 million is {}".format(total))

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