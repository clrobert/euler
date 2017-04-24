import math

def factorial(num):
    for index in range(num, 0, -1):
        num = num * index
    return num

def is_prime(num):
    if n == 0 or n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


