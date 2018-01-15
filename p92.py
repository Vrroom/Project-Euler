import time

t = time.time()
counter = [0]*568

def f(i):
    ss = 0
    while not i == 0:
        ss += (i%10)**2
        i = i//10
    return ss
for i in range(1,10000000):
    counter[f(i)] += 1

c89 = 0

for i in range(1,568):
    t = i
    while True:
        if t == 1 or t == 89:
            break
        t = f(t)
    if t == 89:
        c89 = c89 + counter[i]

print(c89)
