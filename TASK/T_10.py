# Выделите одним махом только текстовую часть оглавления, без тегов
import re

with open('1.txt', 'r', encoding='utf') as f:
    text = f.read()
    p = re.compile(r':(.+)</a>')
    n = re.findall(p, text)
    print(n)
