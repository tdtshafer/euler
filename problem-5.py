"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
UPPER_LIMIT = 20

def main():
	divisible_number = get_divisible_number()
	print("The smallest positive number divisible by all numbers 1-{} is {}".format(UPPER_LIMIT, divisible_number))

def get_divisible_number():
	number = UPPER_LIMIT
	while not is_divisible(number):
		number += UPPER_LIMIT
	return number

def is_divisible(number):
	for x in range(1,UPPER_LIMIT+1):
		if number % x != 0:
			return False
	return True



main()