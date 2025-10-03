import turtle as t

t.speed(1)
t.pensize(5)
t.colormode(255)

# 1. ПРЯМОУГОЛЬНИК (150x75)
t.color("#59D9A5", "#59B8D9")
t.begin_fill()
for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(75)
    t.right(90)
t.end_fill()

t.penup()
t.forward(75)  # 150 (длина прямоугольника) + 10 (расстояние)
t.left(90)    # поворачиваем вверх
t.forward(60) # поднимаемся
t.right(90)   # возвращаем направление вправо
t.pendown()

# 2. ПРАВИЛЬНЫЙ РОМБ (перевернутый)
t.color("blue", "lightblue")
t.lt(210)  # Переворачиваем ромб
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.right(60)    # острый угол
    t.forward(100)
    t.right(120)   # тупой угол
t.end_fill()

t.penup()
t.lt(120)  # поворачиваем вниз
t.forward(80) # опускаемся на 30 пикселей
t.left(90)    # возвращаем направление вправо
t.forward(30)  # 100 (сторона ромба) + 10 (расстояние)
t.pendown()

# 3. ТРАПЕЦИЯ
t.color("red", "lightcoral")
t.begin_fill()
t.forward(60)    # Верхнее основание
t.right(60)      # Угол наклона
t.forward(60)    # Боковая сторона
t.right(120)     # Угол дна
t.forward(120)   # Нижнее основание
t.right(120)     # Угол наклона
t.forward(60)    # Боковая сторона
t.right(60)      # Замыкающий угол
t.end_fill()

t.done()
