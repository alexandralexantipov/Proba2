from tkinter import *

"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
n = n-1 + n-2
 число Фибаначи"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))

ls = [1, 2, [3, 4, [5, [6, 7], 8]]]

def smr(l):
    sm = 0
    for i in l:
        # if type(i) == int:
        if isinstance(i, int):
            sm += i
        else:
            sm += smr(i)
    return sm

print(smr(ls))

def name(nm):
    cnt=0
    def surmame(snm):
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surmame

cnt = 1000
sur = name('Mary')
sur('Petrova')
sur('Ivanova')
sur('Sidorova')
