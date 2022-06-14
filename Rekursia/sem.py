#Максимальное число в списке
def Max(a):
    if len(a) > 1:
        b = Max(a[1:])

        if a[0] < b:
            return b
        else:
            return a[0]

    if len(a) == 1:
        return a[0]

a = [ 3, 6, 4, 10]
res = Max(a)
print("Результат: ", res)