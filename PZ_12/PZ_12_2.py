# Дано целое положительное число. Проверить истинность высказывания: «Данное число является нечетным трехзначным».


from tkinter import *
root = Tk()
root.title("12.2(Сделано по заданию 3.1)")
lbl1 = Label(root, text="Проверка истинности высказывания: «Данное число является нечетным трехзначным»", font=("Arial Bold", 20))
lbl1.grid(column=0, row=0)

lbl2 = Label(root, text="Введите целое положительное число", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1)

tx = Entry(root, width=10)
tx.grid(column=0, row=2)

def clicked():
    n = tx.get()
    n = int(n)
    if (99 < n < 1000 and n % 2) != 0:
        lbl3 = Label(root, text="Да, ваше  число является  нечётным  трёхзначным ", font=("Arial Bold", 10), fg='green')
        lbl3.grid(column=0, row=4)
    else:
        lbl4 = Label(root, text="Нет, ваше число не является нечётным трёхзначным", font=("Arial Bold", 10), fg='red')
        lbl4.grid(column=0, row=4)


bt = Button(root, text='Ввести', command=clicked)
bt.grid(column=0, row=3)


root.mainloop()
