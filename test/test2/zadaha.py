
def Ten(n):
    if n > 1:
        res = Ten(n // 2) + str(n % 2)
        return res
    else:
        return '1'

print("Двоичное число", Ten(13))
