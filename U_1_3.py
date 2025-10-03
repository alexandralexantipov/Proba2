##for i in range(1, 4, 1):  #1, 2, 3
##    print(i, end = ': ')
##    for j in range(1, 6):  # 1, 2, 3, 4, 5
##        print(j, end=' ')
##    print()
##    print('*')
    
    
##print(2,33,55,'Mary')
##print(2,33,55,'Mary', sep= '') # без пробела как конатинация
##print(2,33,55,'Mary', sep= '...', end='---')
##print(2,33,55,'Mary', sep= '...', end='\n')
##print(2,33,55,'Mary', sep= '\n')
##print(222,3322,22255,'Mary')

##for i in range(1, 10, 1):  #1, 2, 3
##    
##    for j in range(1, 10):  # 1, 2, 3, 4, 5
##        print(str(i * j).rjust(2), end=' ')
##    print()

##for i in range(1, 10):  #1, 2, 3
##    
##    for j in range(1, 10):  # 1, 2, 3, 4, 5
##        print(f'{j * i:2}', end=' ')
##    print()

######n = 7
##for n in range(1, 200):
##    for i in range(2, n):
##        if n % i == 0:  # один знак равенства присвоить, а 2 равно сравнить
##            break
##    else:
##        print(n, end=' ')

from turtle import *

colormode(255)
shape('turtle')
red = 252
green = 252
blue = 38
252, 252, 38
color((0, 255, 0,), (red, gr, bl))
pensize(2)

step = 0
long = 200

for long in range(200, 99, -50):
    color((0, 255, 0,), (red, gr, bl))
    begin_fill()
    for _ in range(3):
        fd(long)
        lt(120)
    end_fill()
##    rt(180)
##    long -=50
    red -= 50
    gr -= 50
    bl += 50
    step += 100
    penup()
    goto(step, 0)
    pendown()
##    rt(180)

