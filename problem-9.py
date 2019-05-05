"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def main():
	#not elegant
	for c in range(500):
		for a in range(2, c):
			for b in range(2, c):
				if a**2 + b**2 == c**2:
					if a + b + c == 1000 and a < b:
						print([a, b, c])
						print("Product: {}".format(a*b*c))

main()