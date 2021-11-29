# Дан список размера N, все элементы которого, кроме первого, упорядочены по возрастанию. Сделать упорядоченным,
# переместив первый элемент на новую позицию.
import random

n = int(input('Введите длину списка: '))
spisok = []
i = 0
while i < n:
    spisok.append(random.randint(0, 100))  # В цикле while создаём список размера n с рандомным набором элементов
    i += 1
print('Первоначальный список: ', spisok)
b = spisok[1::]
b.sort()
spisok[1::] = []
for elem in b:  # В список, содержащий только самый первый элемент, добавляем остальные отсортированные элементы списка
    spisok.append(elem)
print('Сортировка списка, кроме 1 - го элемента: ', spisok)
spisok.sort()
print('Сортировка списка полностью: ', spisok)
