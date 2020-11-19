"""
"""

# there is math.gcd, but i guess the implementation is similar
def gcd(x, y):
    """
    Compute the greatest common divisor of x and y using the euclidean algorithm
    """
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    """
    Compute the least common multiple of x and y
    """
    return abs(x*y)//gcd(x, y)

# TODO check: smaller is better, right?
def cir(rs, re, t):
    """
    Find a number n, coprime to t, in the range (rs, re)
    """
    for n in range(rs, re):
        if gcd(n, t) == 1:
            return n

    # TODO handle n not in range
    return 0

# https://en.wikipedia.org/wiki/Modular_exponentiation
def mpow(b, e, m):
    """
    Exponentiation in modular arithmetic
    """
    if m == 1:
        return 0
    c = 1
    for _ in range(e):
        c = (c*b) % m
    return c