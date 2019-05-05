"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
def main():
	sequence_lengths = []
	for x in range(1,int(1e6)):
		number = x
		counter = 0
		while number != 1:
			counter += 1
			if number%2==0:
				number = process_even(number)
			else:
				number = process_odd(number)
		sequence_lengths.append(counter)

	longest = max(sequence_lengths)
	print("Maximum sequence length is {}".format(longest))
	print("Starting number of maximum-length sequence: {}".format(sequence_lengths.index(longest)+1))

def process_even(n):
	return n/2

def process_odd(n):
	return 3*n + 1

main()