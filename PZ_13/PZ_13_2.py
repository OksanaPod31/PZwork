# Составить генератор (yield), который преобразует все буквенные символы в строчные.

s = input("Введите ваше предложение, слово или букву в верхнем регистре, чтобы заметить результат: ")
b = len(s)


def stroc(sentence):
    for i in sentence:
        yield i.lower()


word = stroc(s)

while b:  # Выводим каждый символ
    print(next(word))
    b -= 1
