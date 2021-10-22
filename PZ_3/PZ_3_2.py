# Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).

n = input('Введите первое число: ')
b = input('Введите второе число: ')
c = input('Введите третье число: ')


while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
        b = int(b)
        c = int(c)
        var_1 = n if n > b else b
        high = c if c > var_1 else var_1  # Нахождение максимального числа
        var_2 = n if n < b else b
        low = c if c < var_1 else var_2  # Нахождение миниимального числа
        if low < n < high:
            mid = n
            print(f'Среднее число: {mid}')
        elif low < b < high:
            mid = b
            print(f'Среднее число: {mid}')
        else:
            mid = c
            print(f'Среднее число: {mid}')
    except ValueError:
        print('Ввели неправильно!!')
        n = input('Введите первое число: ')
        b = input('Введите второе число: ')
        c = input('Введите третье число: ')
