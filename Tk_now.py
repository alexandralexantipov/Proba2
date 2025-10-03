# from tkinter import *
#
# WIDTH = 2560  # Параметры экрана
# HEIGHT = 1440
# WIDTH_R = 450
# HEIGHT_R = 250
# root = Tk()  # Создаем главное окно
# # Устанавливаем геометрию окна (центрируем на экране)
# root.geometry(f'{WIDTH_R}x{HEIGHT_R}+{WIDTH//2 - WIDTH_R//2}+{HEIGHT//2 - HEIGHT_R//2 - 25}')
#
# root.mainloop()

from tkinter import *


def read_name():


Name = e.get()  # получаем введенный текст

print(Name)  # выводим введенный текст


def read_city():


City = e2.get()  # получаем введенный текст

print(City)  # выводим введенный текст

window = Tk()

f1 = Frame()

f2 = Frame()

f1.pack()

f2.pack()

m = Label(f1, text="Введите имя : ", bg="grey", font='Courier 16 bold')

m.pack(side=LEFT)

e = Entry(f1, width=20, justify="left", bg="grey",

          fg="brown", font='Courier 18 bold')

e.pack(side=LEFT)

b = Button(f1, text="Ввод", bg="grey", font=('Courier 12 bold'),

           command=read_name)

b.pack()

m2 = Label(f2, text="Введите город: ", bg="grey", font='Courier 16 bold')

m2.pack(side=LEFT)

e2 = Entry(f2, width=20, justify="left", bg="grey",

           fg="brown", font='Courier 18 bold')

e2.pack(side=LEFT)

b2 = Button(f2, text="Ввод", bg="grey", font=('Courier 12 bold'),

            command=read_city)

b2.pack()

window.mainloop()
