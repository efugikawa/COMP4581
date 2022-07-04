# RSA Encryption Cracking
# Elizabeth Fugikawa, summer 2022

# understand how quickly run times for exponential O(2**n) algorithms grow

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
        numOut = int(randFloat * (2**n))
        if numOut >= 2 and isPrime(numOut):
            primeFlag = True
            return numOut


def factor(pq):
    for i in range(2, pq):
        if pq % i == 0 and isPrime(i):
            p = i
            q = int(pq / p)
            return p, q


for n in range(15, 33):
    pq = nBitPrime(n) * nBitPrime(n)
    time1 = time()
    p, q = factor(pq)
    time2 = time()
    t = (time2 - time1) * 1000
    print(n, t, p, q, pq)

#produced trend line y = 8e-05 e^(0.6389x)
#to crack a 1024-bit key, it would take 1.08e+280 milliseconds or 3.42e+269 years