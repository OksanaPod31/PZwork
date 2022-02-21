# Найдите слова, в которых есть русская буква, а когда-нибудь за ней цифра
import re

p = re.compile(r'^\w+[0-9]$')

print('Задание 3 с цифрой:', p.findall('скучно2'))
print(p.findall('скучно'))  # Задание 3 без цифры
print(p.findall('ску%чно2'))  # Задание 3 с цифрой и другим символом
