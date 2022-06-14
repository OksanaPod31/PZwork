# Кол-во отрицательных чисел в списке
li = [3, 4, -2, -4]

def sum1(lst):
    t = 0
    for elem in lst:
        if isinstance(elem, list):
            t += sum1(elem)
        else:
            if elem < 0:
                t += 1
    return t
print("Сумма элементов равна:", sum1(li))