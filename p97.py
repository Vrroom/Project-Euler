import numpy as np

def pow_mod_m(a,e,m):
    if e == 0:
        return 1
    b = 1 # keeps track of how many times odd e came
    while e > 1:
        if e % 2 == 0:
            a = a*a % m
            e = e/2
        else:
            b = a*b % m
            a = a*a % m
            e = (e-1)/2
    return a*b % m


