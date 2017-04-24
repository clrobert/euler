"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def sum_digits(num):
    num_string = str(num)

    running_total = 0

    for char in num_string:
        running_total = running_total + int(char)

    return running_total

def factorial(num):
    for index in range(num, 0, -1):
        num = num * index
    return num

example = factorial(10)
print(example)
print(sum_digits(example))

example = factorial(100)
print(example)
print(sum_digits(example))
