"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def main():

	products = get_products(999, 999)
	print("The largest palindrom made from the product of two 3-digit numbers is {}".format(max(products)))

def get_products(a, b):
	products = set()
	for x in range(a):
		for y in range(b):
			product = (a-x)*(b-y)
			if is_palindrome(product):
				print("Adding {} x {}".format(a-x, b-y))
				products.add(product)
	return products

def is_palindrome(number):
	number_string = str(number)
	return number_string == number_string[::-1]

main()