# Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами);
import re


with open('1.txt', 'r', encoding='utf') as f:
    text = f.read()
    p = re.compile(r'<a href=.+')
    n = re.findall(p, text)
    print(n)
