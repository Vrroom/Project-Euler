# p65.py - Based on the continued fraction fundamental recurrence
# relation which states: p_n*q_{n-1} - p_{n-1}*q_n = -1^{n+1}

def e_partial_denom():
    i = 1
    yield 2 
    while True:
        if i % 3 == 0 or i % 3 == 1:
            yield 1
        else: 
            yield 2*(i+1)//3
        i = i+1

def convergent(G):
    h = [1,0]
    k = [0,1]
    while True:
        an = next(G)
        th = [an*h[0] + h[1],h[0]] 
        tk = [an*k[0] + k[1],k[0]]
        h = th
        k = tk
        yield [h[0],k[0]]

def xgcd(a,b):
    aa = [1,0]
    bb = [0,1]
    q = None
    r = None
    out = []
    while True:
        q = a//b
        a = a%b
        aa[0] = aa[0] - q*aa[1]
        bb[0] = bb[0] - q*bb[1]
        if a == 0:
            out.append(aa[1])
            out.append(bb[1])
            return out
        q = b//a
        b = b%a
        aa[1] = aa[1] - q*aa[0]
        bb[1] = bb[1] - q*bb[0]
        if b == 0:
            out.append(aa[0])
            out.append(bb[0])
            return out
