from functools import reduce
from math import gcd

def factors(n: int, only_primes: bool = True):
    factors = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
    return factors if not only_primes else [x for x in factors if isPrime(x)]


def pollard_factors(n: int):
    """
    Integer factorization using Pollard-Pho algorithm.
    Return -1 if n is a prime.
    Else return one of the factors of n
    """
    a = 2
    b = 2
    d = 1

    while d == 1:
        a = (a ** 2 + 1) % n
        b = ((b ** 2 + 1) ** 2 + 1) % n
        d = gcd(a - b, n)

    if d == n:
        return -1
    else:
        return d


def get_factor_power(factor:int, n:int) -> int:
    assert n % factor == 0
    idx = 1
    while n % (factor ** idx) == 0:
        idx += 1

    return idx - 1


def isPrime(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True



def legenre(a: int, n: int) -> int:
    assert a % n != 0
    assert isPrime(n)
    if (a ** ((n - 1)/2)) % n == 1:
        return 1
    elif (a ** ((n - 1)/2)) % n == n - 1:
        return -1
    else:
        assert False


def jacobi(a: int, n:int) -> int:

    if a % n == 0:
        return 0

    n_factors = factors(n)
    n_factors = [factor for factor in n_factors if isPrime(factor)]

    n_e = [get_factor_power(x, n) for x in n_factors]
    res = 1
    for (p, e) in zip(n_factors, n_e):
        res *= (legenre(a, p) ** e)

    return res


def totient(n: int) -> int:
    """Find the Euler Totient of a number."""

    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1

    return amount

def discrete_log(g: int, h: int, n: int):
    """Solve the DLP problem. Find x such that g^x = h mod n."""
    for x in range(1, n):
        if g ** x % n == h:
            return x

    return -1
