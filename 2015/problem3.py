


# PDL:: Sieve:
# Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
# Initially, let p equal 2, the first prime number.
# Starting from p, count up in increments of p and mark each of these numbers greater than p itself
# in the list. These will be multiples of p: 2p, 3p, 4p, etc.; note that some of them may have already been marked.
# Find the first number greater than p in the list that is not marked. 
# If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.

def largestPrimeFactor(num):


def main():
	solution = largestPrimeFactor(600851475143)
	print solution

main()

