
import math

def R(num):
    if num<0:
        return -1
    if num==0:
        return 0
    n = 0
    num2 = num

    while num2>0:
        n = n+1
        num2 = num2//10

    s = num%10
    res = s * int(math.pow(10, n-1))
    return res + R(num//10)

print(R(1234))