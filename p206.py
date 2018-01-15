import time
from threading import Thread

t = time.time()

def match(num):
    dig = 9
    while not num == 0:
        if not num % 10 == dig:
            return False
        num = num//100
        dig = dig - 1
    return True

def three_step():
    for i in range(101010103,138902662,10):
        if match(i**2):
            flag = False
            print(i)
            break

thr = Thread(target=three_step)
thr.daemon = True
thr.start()

for i in range(101010107,138902662,10):
    if match(i**2):
        print(i)
        break
print(time.time()-t)
