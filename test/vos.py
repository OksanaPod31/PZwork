import math

def r(a, b):
    if a>0:
        s = a%2
        return r(a//2, b+1) + int(s*math.pow(10,b))
    else:
        return 0

res = r(126, 0)
print("Результат: ", res)
