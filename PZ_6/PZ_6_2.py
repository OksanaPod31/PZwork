# Дано число R и список размера N. Найти два различных элемента списка, сумма которых наиболее близка к числу R,
# и вывести эти элементы в порядке возрастания их индексов (определение наиболее близких чисел -  то есть такой элемент
# Ak, для  которого величина |Ak - R| является минимальной).
import random


r = int(input('Введите число R: '))
n = int(input('Введите длину списка: '))
spisok = []
i = 0

while i < n:
    spisok.append(random.randint(0, 100))  # В цикле while создаём список размера n с рандомным набором элементов
    i += 1
spisok.sort()  # Сортируем список, чтобы индексация в spisok и последующем списке lit совпадала
print('Исходный список: ', spisok)

lit = []
for elem in spisok:  # Создаём новый список lit, куда добавляем разность |Ak - R | для определения близости элементов
    razn = elem - r  # в списке к числу R. Отрицательные делаем положительными, т.к. при сравнении они будут
    if razn < 0:     # давать неправильный результат.
        razn *= (-1)
    lit.append(razn)
print('Список разности Ak - R: ', lit)
a = min(lit)      # Ищем два наименьших элемента из списка с разностью числа Ak и R, и находим их индексы, чтобы потом
c = lit.index(a)  # впоследствии обратиться по индексам к элементам в исходном списке
lit.remove(a)
b = min(lit)
lit.append(a)  # Возвращаем a, чтобы индексация была правильной, без неё она сдвинется на 1 значение
lit.sort()
v = lit.index(b)
num1 = spisok[c]
num2 = spisok[v]

print('Два элемента, наиболее приближённых к числу R: ', num1, num2)
