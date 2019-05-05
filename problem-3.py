"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def main():
	number = 600851475143
	prime_factors = get_prime_factors(number)
	print("The largest prime factor of {} is {}".format(
		number,
		max(prime_factors),
	))

def get_prime_factors(number):
	prime_factors = []
	factor = next_prime()
	while not is_prime(number):
		if number % factor == 0:
			number = int(number / factor)
			prime_factors.append(factor)
		else:
			factor = next_prime(factor)

	prime_factors.append(number)
	print(prime_factors)
	return prime_factors

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