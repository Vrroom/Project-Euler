from functools import reduce
import operator

def helper(n):
    primes = {}
    d = 2
    while d*d <= n:
        while n%d == 0:
            try:
                primes[d] = primes[d] + 1
            except KeyError:
                primes[d] = 1
            n //= d    
        d = d + 1
    if n > 1:
        try:
            primes[n] = primes[n] + 1
        except KeyError:
            primes[n] = 1
    phi_p = []
    for k, v in primes.items():
        phi_p.append(k**v - k**(v-1))
    return phi_p

def opt(n):
    d = 2
    prod = 1
    while d*d <= n:
        while n%d == 0:
            n //= d
        prod = prod*(d/(d-1))
        d = d+1
    if n > 1:
        prod = prod*(n/n-1)
    return prod 

def phi(n):
    return reduce(operator.mul,helper(n),1)


m = 0
for n in range(1000000,0,-1):
    if m < opt(n):
        m = opt(n)
        print(n)

