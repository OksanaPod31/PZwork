__all__ = ['circle_perimetr', 'circle_area']
from math import pi as p


def circle_perimetr(rad=5):
    return print('Длина окружности: ', 2 * p * rad)


def circle_area(rad=5):
    return print('Площадь окружности: ', p * rad ** 2)