"""
The sum of the squares of the first ten natural numbers is:
				1^2 + 2^2 + ... + 10^2 = 385


The square of the sum of the first ten natural numbers is:
				(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def main():
	limit = 100
	squares_sum = get_squares_sum(limit)
	sum_squared = get_sum_squared(limit)

	print("The sum of the squares: {}".format(squares_sum))
	print("The square of the sums: {}".format(sum_squared))
	print("The difference: {}".format(sum_squared - squares_sum))

def get_squares_sum(limit):
	return sum([x**2 for x in range(1,limit+1)])

def get_sum_squared(limit):
	return sum(range(1, limit+1))**2

main()