# Из исходного текстового файла (expansion.txt) выбрать имена файлов, соответствующих типам: css, xls, html, py, xml.
# Посчитать кол-во полученных элементов.

import re  # Импортируем модуль re

with open('textprac.txt', 'r', encoding='utf') as f:
    text = f.read()
    p = re.compile(r"\b(.+)(\.css|\.xls|\.html|\.py|\.xml)\b")
    n = re.findall(p, text)  # Находим совпадения с шаблоном по всему файлу, получая список элементов
    c = len(n)  # Кол-во найденных элементов
    k = 0
    s = []
    while k < c:
        s.append(n[k][0])
        k += 1

    s = ", ".join(s)

    print(f'Файлы, соответствующие типам css, xls, html, py, xml:\t {s}')
    print(f'Кол-во файлов: {c}')
