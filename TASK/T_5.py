# Найдите слова, которые начинаются на гласную (\b — граница слова)
import re

p = re.compile(r'\b[ауоыиэяюеё].+?\b', re.I)

print(p.findall('Называй день  Яна олег Bad'))
