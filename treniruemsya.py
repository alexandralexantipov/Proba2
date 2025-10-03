import turtle as t

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
t.hideturtle() # hide - скрыть
t.color("green")
##t.rt(90)
t.pensize(5)
for i in range(4, 56, 4):
    t.fd(i)
    t.rt(90)
t.rt(270)    
for i in range(52, 0, -4):
    t.fd(i)
    t.rt(90)

