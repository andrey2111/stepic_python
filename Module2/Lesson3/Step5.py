import itertools


def isSimple(n):
    d = n - 1
    while d > 1:
        if n % d == 0:
            return False
        d -= 1
    return True

def primes():
    for i in range(2, 100500):
        if isSimple(i):
            yield i


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
