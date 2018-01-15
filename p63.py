import numpy as np

total = 0
for i in range(1,10):
    n = 1
    while (1-(1/n)) <= np.log10(i):
        total = total+1
        n = n+1

print(total)
