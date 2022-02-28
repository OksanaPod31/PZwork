#  В матрице найти среднее арифметическое последних 2 столбцов.
import random
matr = [[random.randint(0, 90)for _ in range(3)] for y in range(1, 4)]
print('Начальный список: ', matr)

matrnew = [matr[i][j] for i in range(0, 3) for j in range(1, 3)]  # Составляем список с элементами последних 2 столбцов
c = sum(matrnew) / len(matrnew)

print('Элементы 2 последних столбцов: ', matrnew)
print('Среднее арифметическое: ', c)
