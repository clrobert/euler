
"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

"""
Note: the clue was in the name. Lattice paths. This is a binomial theorem problem.
"""

from mylib import factorial

def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


ans = binomial(20,20)
print(ans)

