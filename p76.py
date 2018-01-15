import numpy as np
import itertools

def partition(n):
    poly = np.ones(n+1)
    for i in range(2,n+1):
        d = 0
        m = np.zeros(n+1)
        while d*i <= n:
            m[n-d*i] = 1
            d = d+1
        poly = np.polymul(m,poly)[-(n+1):]
    return poly[0]

def erasthenes():
    D = {} # Map each composite number to its first found prime factor
    for q in itertools.count(2):
        p = D.pop(q,None)
        if p is None:
            yield q
            D[q*q] = q
        else:
            x = p+q
            while x in D:
                x = x + p
            D[x] = p

def prime_partition(n):
    poly = np.ones(1)
    for i in erasthenes():
        if i > n:
            break
        d = 0
        m = np.zeros(n+1)
        while d*i <= n:
            m[n-d*i] = 1
            d = d+1
        poly = np.polymul(m,poly)[-(n+1):]
    return poly[0]

