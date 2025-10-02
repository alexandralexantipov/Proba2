import turtle as t
import time  # Змодуль замедлять выполнение программ (время) 
##t.speed(0)
t.ht()
t.colormode(255)  # Если для конс.черепашки, то этот метод не нужен - закомментировать


""" Используем print для получения и внесения диапазона в range +
в диапазоне задаём увеличение перехода от цвета к цвету с большим оттенком"""

##print(list(range(40, 0, -10)))  # Отображение выполнения данных в
                                  #скобках выводит в консоль это будет [40, 30, 20, 10], чтобы в дальнейшем напрямую
                                  #вставлять в значения цикла - range(40, 0, -10) ""
##r= 40  # После получения данных при помощи print (выше) переменная не требуется
t.pensize(5)
t.speed(0)
#for j in range(4): # После получения данных при помощи print (выше) функцию заменяем на (ниже) не требуется 
for j in range(40, 0, -10):  # Используем диапазон
    for i in range(6):
        t.color(255, 165, j * 6)  # j * 6 - для перехода цвета в диапазоне
        t.fillcolor(162, j * 6, 255)
        t.begin_fill()
        t.circle(j)
        t.end_fill()
        t.rt(60)
    #r = r - 10  # После получения данных при помощи print (выше) переменная не требуется


""" Ввод с клавы количеством углов для фигуры в цикле """

##t.ht()
##t.speed(8)
##t.colormode(255)

##a = input("Введите количество углов ")
##a = int(a)
##t.color("green")
##t.begin_fill()
##for i in range(a):
##    t.forward(80)
##    t.left(360/a)
##t.end_fill()

""" Лабиринты с шагом и зеркально """

##t.ht() # t.hideturtle() # hide - скрыть
##t.color("green")
####t.rt(60)
##t.pensize(5)
##for i in range(4, 56, 4):
##    t.fd(i)
##    t.rt(90)
##t.rt(270)    
##for i in range(52, 0, -4):
##    t.fd(i)
##    t.rt(90)
##

""" Цветок (и рядом) с вложеннымb циклами """

# Один цветок в цикле

##t.ht()
##r = 40
##t.pensize(4)
##t.speed(0)
##t.color("#FFA500")
##t.fillcolor("#A200FF")
##for j in range(4):
##    for i in range(6):
##        t.begin_fill()
##        t.circle(r)
##        t.end_fill()
##        t.rt(60)
##    r = r - 10

# Три цветка рядом с вложенными циклами

##t.speed(0)
##t.ht()
##r = 20
##t.pensize(4)
##t.color("#FFA500", "#A200FF") # Контур и заливка
####t.fillcolor("#A200FF")  # Только заливка
##for j in range(4):
##    for i in range(6):
##        t.begin_fill()
##        t.circle(r)
##        t.end_fill()
##        t.rt(60)
##    r = r - 5
##t.pu()
##t.fd(80)
##r = 20
##t.pd()
##for j in range(4):
##    for i in range(6):
##        t.begin_fill()
##        t.circle(r)
##        t.end_fill()
##        t.rt(60)
##    r = r - 5
##t.pu()
##t.fd(80)
##r = 20
##t.pd()
##for j in range(4):
##    for i in range(6):
##        t.begin_fill()
##        t.circle(r)
##        t.end_fill()
##        t.rt(60)
##    r = r - 5

# 3 Цветка в одном цикле (сокращённая программа за счёт цикла)

##t.speed(0)
##t.ht()
##r = 20
##t.pensize(4)
##t.color("#FFA500", "#A200FF") # Контур и заливка
####t.fillcolor("#A200FF")  # Только заливка
##for k in range(3):
##    #print("_____k = " + str(k))  # Отображение выполнения этой переменной в программе в консоли
##    for j in range(4):
##        #print("__j = " + str(j))  # Отображение выполнения этой переменной в программе в консоли
##        for i in range(6):
##            #print("i = " + str(i))  # Отображение выполнения этой переменной в программе в консоли
##            t.begin_fill()
##            t.circle(r)
##            t.end_fill()
##            t.rt(60)
##            #time.sleep(0.1) # Замедляет (метод модуля time выполнение в секундах)
##        r = r - 5
##    t.pu()
##    t.fd(80)
##    t.pd()
##    r = 20




