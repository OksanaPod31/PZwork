def calc(b):
    if b == []:
        return 0
    else:
        count = calc(b[1:])
        if b[0] < 0:
            count = count+1
        return count

s = [1, -2, 3, -4]
n = calc(s)
print(n)