def Max(a):
    if len(a)>1:

        Max1 = Max(a[1:])


        if a[0]<Max1:
            return Max1
        else:
            return a[0]

    if len(a)==1:
        return a[0]


a = [ 3, 6, 4, 10]
res = Max(a)
print("Результат: ", res)