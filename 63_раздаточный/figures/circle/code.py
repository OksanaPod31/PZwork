__all__ = ['circle_perimetr', 'circle_area']
from math import pi as p

default_rad = 5


def circle_perimetr():
    rad = int(input('Введите радиус, если это необходимо, в ином случае введите 0: '))
    if rad:
        return print('Длина окружности: ', 2 * p * rad)
    if rad == 0:
        return print('Длина окружности: ', 2 * p * default_rad)


def circle_area():
    rad = int(input('Введите радиус, если это необходимо, в ином случае введите 0: '))
    if rad:
        return print('Площадь окружности: ', p * rad ** 2)
    if rad == 0:
        return print('Площадь окружности: ', p * default_rad ** 2)
