# Найдите пустые строчки
import re

with open('1.txt', 'r', encoding='utf') as f:
    text = f.read()
    p = re.compile(r"[/^\s*$]")
    n = re.findall(p, text)
    print(n)
