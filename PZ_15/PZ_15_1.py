#  В матрице элементы кратные 3 увеличить в 3 раза.
import random
matr = [[random.randint(0, 15)for _ in range(3)] for y in range(1, 4)]
print('Начальный список: ', matr)
matrnew = [matr[i][j] * 3 if matr[i][j] % 3 == 0 else matr[i][j] for i in range(0, 3) for j in range(0, 3)]


def posl(ls, k):
    for i in range(0, len(ls), k):
        yield ls[i: i + k]


print('Результат: ', list(posl(matrnew, 3)))
