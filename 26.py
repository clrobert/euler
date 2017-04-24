"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def longest_recurring_cycle():
    pass


def get_rhs(num, denom):
    num = float(num)
    denom = float(denom)
    frac = float(num/denom)
    rhs = str(frac).split(".")[1]
    return rhs


def get_cycle(substr):
   """Use floyd's algo."""
   pass


longest_cycle = 0
longest_index = 0

for index in range(1, 1000):
    sub_str = get_rhs(1, index)
    len_cycle = len(get_cycle(sub_str))
    if len_cycle > longest_cycle:
        longest_index = index
        longest_cycle = len_cycle

print(longest_index)
print(longest_cycle)

