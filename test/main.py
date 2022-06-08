li = [3,4]
li2 = 3
def sum1(lst):
    t = 0
    for elem in lst:
        if (type(elem) == type("list")):
            t += sum1(elem)
        else:
            t += elem
    return t
print("Сумма элементов равна:", sum1(li))