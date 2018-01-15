import numpy as np

pairs = np.loadtxt('p099_base_exp.txt',delimiter=",")
ln = 0
[n,m] = pairs.shape
for i in range(n):
    if pairs[i][1]*np.log(pairs[i][0]) > m:
        m = pairs[i][1]*np.log(pairs[i][0])
        ln = i+1
    
print(ln)
