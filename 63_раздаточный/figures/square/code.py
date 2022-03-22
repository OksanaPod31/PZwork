__all__ = ['squre_perimetr', 'squre_area']
a = 15


def squre_perimetr():
    side = int(input('Введите сторону, если это необходимо, в ином случае введите 0: '))
    if side:
        return print('Периметр квадрата: ', 4 * side)
    if side == 0:
        return print('Периметр квадрата: ', 4 * a)


def squre_area():
    side = int(input('Введите сторону, если это необходимо, в ином случае введите 0: '))
    if side:
        return print('Площадь квадрата', side ** 2)
    if side == 0:
        return print('Площадь квадрата', a ** 2)
