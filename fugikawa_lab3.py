# RSA Cracking
import random
from math import sqrt
from time import time


def isPrime(p):
    for i in range(2, int(sqrt(p)) + 1):
        if (p % i) == 0:
            return False
    return True


def nBitPrime(n):
    primeFlag = False
    while primeFlag is False:
        randFloat = random.random()
        numOut = randFloat * (2**n)
        if numOut >= 2 and isPrime(numOut):
            return int(numOut)
        else:
            return nBitPrime(n)


def factor(pq):
    for i in range(int(sqrt(pq)), 2, -1):
        if pq % i == 0:
            p = i
            q = int(pq / p)
            return p, q


for n in range(15, 19):
    pq = nBitPrime(n) * nBitPrime(n)
    time1 = time()
    p, q = factor(pq)
    time2 = time()
    t = (time2 - time1) * 1000
    print(n, t, p, q, pq)
