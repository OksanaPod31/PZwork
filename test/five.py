def power(b, e):
    if (e == 1):
        return (b)
    if (e != 1):
        return (b * power(b, e - 1))
b = int(input("Введите число: "))
e = int(input("Введите степень: "))
print("Результат:", power(b, e))