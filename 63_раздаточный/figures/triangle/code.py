__all__ = ['triangle_perimetr', 'triangle_area']

from math import sqrt as s


def triangle_perimetr(a=7, b =2, c=8):
    return print('Периметр треугольника: ', a + b + c)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) / 2
    return print('Площадь треугольника', s(p * (p - a) * (p - b) * (p - c)))
