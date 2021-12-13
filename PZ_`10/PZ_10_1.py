# Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных
# и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Среднее арифметическое элементов:
# Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов:


import random

with open('file1.txt', 'w', encoding='utf-8') as f:
    n = int(input('Введите кол-во значений: '))
    num = [random.randint(-100, 100) for i in range(n)]  # Рандомный набор чисел

    lis = ''  # Преобразуем list в str
    for x in num:
        lis += str(x) + ' '
    f.write(lis)

with open('file2.txt', 'w', encoding='utf-8') as s:
    with open('file1.txt', 'r', encoding='utf-8') as d:
        re = d.read().split()

    res = ''
    for i in re:
        res += str(i) + ' '

    spisoc = [int(elem) for elem in res.split() if elem.isdigit]
    dlina = len(spisoc)
    cube = []

    for x in spisoc:
        i = spisoc.index(x)
        if i == 0:  # Т.к. [i - 1] - будет последнее число из списка
            ff = 0
            sf = spisoc[1]
            cub = ff ** 2 + (2 * ff * sf) + sf ** 2  # Квадрат суммы
            cube.append(cub)

        elif i == dlina - 1:  # Т.к. за [i + 1] нет чисел в списке, что выдаст ошибку
            ff = spisoc[i - 1]
            sf = 0
            cub = ff ** 2 + (2 * ff * sf) + sf ** 2
            cube.append(cub)
        else:
            ff = spisoc[i - 1]
            sf = spisoc[i + 1]
            cub = ff ** 2 + (2 * ff * sf) + sf ** 2
            cube.append(cub)

    lis_2 = ''
    for y in cube:
        lis_2 += str(y) + ' '
    print(lis_2)

    sam = sum(spisoc)
    sr = str(sam / dlina)

    s.write(f'Исходные данные: {str(res)}\n')
    s.write(f'Количество элементов: {str(len(re))}\n')
    s.write(f'Среднее арифметическое элементов: {sr}\n')
    s.write(f'Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов: {lis_2}')
