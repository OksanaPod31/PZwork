__all__ = ['triangle_perimetr', 'triangle_area']

from math import sqrt as s

a = 7
b = 2
c = 8


def triangle_perimetr():
    one = int(input('Введите первую сторону, если это необходимо, в ином случае введите 0: '))
    two = int(input('Введите вторую сторону, если это необходимо, в ином случае введите 0: '))
    three = int(input('Введите третью сторону, если это необходимо, в ином случае введите 0: '))
    if one + two + three > 0:
        return print('Периметр треугольника: ', one + two + three)
    if one + two + three <= 0:
        return print('Периметр треугольника: ', a + b + c)


def triangle_area():
    print('При вводе отрицательных или цифр впермешку с нулями возникнет ошибка, т.к. нельзя вычислить корень из подобных чисел')
    one = int(input('Введите первую сторону, если это необходимо, в ином случае введите 0: '))
    two = int(input('Введите вторую сторону, если это необходимо, в ином случае введите 0: '))
    three = int(input('Введите третью сторону, если это необходимо, в ином случае введите 0: '))
    if one or two or three:
        p = (one + two + three) / 2
        return print('Площадь треугольника', s(p * (p - one) * (p - two) * (p - three)))
    if not(one or two or three):
        p = (a + b + c) / 2
        return print('Площадь треугольника', s(p * (p - a) * (p - b) * (p - c)))
