#Фибоначчи
def f(n):
    if n in (1, 2):
        return 1
    return f(n - 1) + f(n - 2)

n = 5

print(f(n))