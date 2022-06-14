#Сумма элементов списка с поддержкой вложенного спсика
li = [[3, 4], [5, 2]]

def sum1(lst):
    t = 0
    for elem in lst:
        if isinstance(elem, list):
            t += sum1(elem)
        else:
            t += elem
    return t
print("Сумма элементов равна:", sum1(li))