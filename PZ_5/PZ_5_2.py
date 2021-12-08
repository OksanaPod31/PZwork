# Описать функцию PowerA234(A, B, C, D),вычисляющую вторую, третью и четвёртую степень числа А и возвращающую эти
# степени соответственно в переменные B,C и D(A - входной, B,C,D - выходные параметры; все параметры являются
# вещественными). С помощью этой функции найти вторую, третью, четвёртую степень пяти данных чисел.

def power_a234(a):
    b = pow(a, 2)  # Возведение в степень
    c = pow(a, 3)
    d = pow(a, 4)
    print('Вторая степень: ', b, 'Третья степень:', c, 'Четвёртая степень: ', d, sep="\n")


def put():
    numb = input('Введите ваше число: ')
    while type(numb) != int:  # Проверка исключений
        try:
            numb = int(numb)
        except ValueError:
            print('Неправильно ввели!')
            numb = input('Введите ваше число: ')
    return power_a234(numb)


k = 0
for k in range(5):  # Вызов функции 5 раз для ввода 5 чисел
    put()