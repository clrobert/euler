"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?"""


def is_special_div(n):
    for i in range(21, 0, -2):
        if n % i is not 0:
            return False

    return True


def find_smallest_special_div():
    for i in range(2520, pow(10, 8)):
        if is_special_div(i):
            return i

n = find_smallest_special_div()
print(n)
