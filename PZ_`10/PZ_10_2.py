# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое, количество знаков пунктуации в
# первых четырёх строках. Сформировать новый файл, в который поместить текст в стихотворной форме выведя строки
# в обратном порядке.


with open('text18-18.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print("\tСодержимое файла:   ", text, sep="\n")
    x = 1

    with open('text18-18.txt', 'r', encoding='utf-8') as s:
        tex = s.readlines()
        p = 0
        k = 0
        for i in tex:
            st = ['.', ',', ':', ';', '—', '…', '!', '?']
            for char in st:
                if char in i:
                    print('\tВстречаемые символы: ', char)
                    k += 1
            p += 1
            if p == 4:
                break
            if p != 4:
                continue
        print('Количество символов пунктуации в первых 4 строках: ', k)

with open('text18-2.txt', 'w', encoding='utf-8') as t:
    with open('text18-18.txt', 'r', encoding='utf-8') as tes:
        nad = tes.readlines()
        nad[-1] = 'Товарищей считать.\n'
        print(nad)
    nad.reverse()
    sl = " ".join(nad)
    t.write(f'\tПеревёрнутое стихотворение:\n {sl}', )
