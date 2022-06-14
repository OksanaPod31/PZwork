#Возведение x в степень y
def Step(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * Step(a, b - 1))

print("Результат:", Step(2, 3))