def prop(f, num):
    while not num < 10:
        a = num % 10
        num = num//10
        b = num % 10
        if f(a,b):
            return False
    return True
            
count = 0
n = 10000000-1
for i in range(1,10000000):
    if (not prop(lambda a,b: a > b, i)) and (not prop(lambda a,b: a < b, i)):
        count = count + 1
    if (count/i) == 0.99:
        print(i)
        break

