#Реверсирование числа
def R(n):
    s = 0
    i = n
    d = n
    while i != 0:
        s += 1
        i //= 10
    s -= 1
    if s == 0:
        res = str(n)

        return res
    else:
        d %= 10
        res = str(d) + R(n // 10)
        return  res
print(R(234))