li = [[1,2,3,4], [3, 5]]
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print("Сумма элементов равна:", sum1(li))