##import 
""" Модуль turtle и методы """
##turtle.forward(100) # рисует линию слева направо по значению в пикселях
##turtle.left(90)  # поворачивает влево курсор на "угол" указанный в значении в пикселях
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(100)
##turtle.left(90)
##turtle.left(45)
##turtle.forward(141.42)
##turtle.left(135)
##turtle.forward(100)
"""Как вычислить диагональ квадрата
Формула:
d = a × √2 (100 х √2 = 
где:
d — длина диагонали,
a — длина стороны квадрата,
√2 (корень из двух) — это константа, примерно равная 1.4142"""

""" Циклы """

# 1. Квадрат
##import turtle

##for i in range(4):
##    print(i)
##    turtle.forward(100)
##    turtle.left(90)
    
# range (двоеточие обязательно, а в скобках количество повтора)
# простыми словами это «генератор чисел» для циклов
""" Cпециальный тип (или точнее, неизменяемая последовательность)
    ,для генерации последовательности целых чисел. """
# for i in в Python — это цикл перебора.
"""Он берёт элементы из коллекции (списка, строки, диапазона и т.д.)
и по очереди присваивает их переменной i, выполняя код внутри цикла
для каждого элемента.""" 

# 2. Равносторонний треугольник (правильные фигуры)
##for i in range(3):
##    turtle.forward(100)
##    turtle.left(120)
"""Формула для вычисления угла поворота:
Угол поворота = 180 - (внутренний угол фигуры)
Сумма внутренних углов треугольника: 180°
Каждый угол равностороннего треугольника: 60°
Угол поворота черепахи: 180 - 60 = 120°
Черепаха движется по внешним углам.
Чтобы она «завернула» на следующий угол фигуры,
ей нужно повернуться на внешний угол, который
равен 180 - внутренний_угол."""

# 3. Равносторонний шестиугольник
##import turtle
##Ugol = 6
##for i in range(Ugol):
##    turtle.shape("turtle") # ("circle"), ("square"), ("triangle"),("classic")
##    turtle.forward(10)  # или back
##    turtle.left(360 / Ugol)  # или right
    
# Пример из интернета: 
##fruits = ["apple", "banana", "cherry"]
##for fruit in fruits:  # fruit = "apple", потом "banana", потом "cherry"
##    print(f"I like {fruit}")
##print("Loop is finished! - Цикл закончен!")
##""" сумма внутренних углов любого n-угольника
##всегда равна 180° × (n - 2) """
##a = [10, 11, 12, 14, 16, 11, 13, 10]
##b = [45, 45, 45, 45, 45, 45, 45, 45]
##
##t = turtle.Turtle()
##t.speed(3)
##
### Запоминаем начальную позицию
##start_x, start_y = t.position()
##
##for i in range(8):
##    t.forward(a[i])
##    t.left(b[i])
##
### Возвращаемся в начальную точку
##t.goto(start_x, start_y)
##
##turtle.done()

""" Закрашиваем фигуру с вводом кол-ва углов
с клавы и переменную после ввода переводим в числовое значение"""
##import turtle
##
##Ugol = input("введите количество углов ")
##Ugol = int(Ugol)
##Col = input("введите цвет на ангийском ")
##turtle.color(Col)
##turtle.begin_fill()
##for i in range(Ugol):
####    turtle.shape("classic") # ("circle"), ("square"), ("triangle"),("turtle")
##    turtle.forward(80)  # или back
##    turtle.left(360 / Ugol)  # или right
##turtle.end_fill()


##t.shape("turtle")
##current_x = t.xcor()  # узнать текущую координата x (горизонталь)
##current_y = t.ycor()  # узнать текущую координата y (вертикаль)
##print(f"Текущая позиция: ({current_x}, {current_y})")
##t.penup()
##t.goto(-75, 100)  # x=150, y=100
##t.pendown()
##t.right(90)
##t.begin_fill()
##t.color('blue', 'red')  # первый цвект линии, второй цвет закрашивания
##t.circle(50)
##t.end_fill()
##t.penup()
##t.fd(100)  # forward можно писать сокращённо fd
##t.pendown()
##t.begin_fill()
##t.color('blue', 'yellow')  ##t.color(245/255, 66/255, 179/255) ##t.color('#000000', '#E77CFA')
##t.circle(50)
##t.end_fill()
##t.penup()
##t.fd(100)  
##t.pendown()
##t.begin_fill()
##t.color('blue', 'green')
##t.circle(50)
##t.end_fill()


##import turtle as t
##
### Запрос радиуса
##r = int(input("Введите радиус кругов: "))
##
### СПИСОК цветов (можно заменить на КОРТЕЖ)
##colors = ['#000000', '#7f7f50', '#fefe9f']  # квадратные скобки - список
##
##for i in range(3):
##    t.begin_fill()
##    t.color(colors[i])  # берем i-й цвет из списка
##    t.circle(r)
##    t.end_fill()
##    t.penup()
##    t.forward(50)
##    t.pendown()

import turtle
Ugol = 5
turtle.begin_fill()
for i in range(Ugol):
    turtle.forward(100)
    turtle.right(360 * 2 / Ugol)
turtle.end_fill()

##i = 0
##
##i +=1 # i = i + 1
##i +=1
##i +=1
##i +=1
##i +=1
##i +=1
##i +=1
##i +=1
##i +=1
##i +=1
##print(i)

##for i in 22, 33, 44, 55:
##    print(i, 'Yes')
##    print(i)
##print(list(range(0, 10+1, 2)))  # start = 0,
##i = 0
##for _ in range(10):
##    i += 1
####    print(i)
##print(i)
##print(list(range(10)))

##i = 0
##for ico in 0, 1, 2, 3, 4, 5, 6, 7, 8, 9:
##    i += 1
##print(i)

##import turtle as tr

##from turtle import *
##
##colormode(255)

##shape('turtle')
##pensize(3)
##color('green', 'yellow')
##color(100, 100, 50)
##color('#00f000')
##speed(1)

##fd(200) # forward
####mainloop()
##lt(120)  # left против часовой стрелки будет поворт на 120 градусов
##fd(200)
##lt(120)
##fd(200)
##lt(120)
##begin_fill()
##for i in range(1, 6, 2):  # 1, 3, 5
##    pensize(i)
##    fd(200)
##    lt(120)
##end_fill()

