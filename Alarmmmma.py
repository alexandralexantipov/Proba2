from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg

pg.init()
pg.mixer.music.load("music.mp3")

def start():
    global alarm_time
    alarm_time = alarm.get().strip()
    messagebox.showinfo('Установка времени',
                        f'Будильник установлен на '
                        f'{alarm_time}')


def stop():
    global alarm_time
    alarm_time = ""
    alarm.delete(0, END)
    pg.mixer.music.stop()
    messagebox.showinfo('Предупреждение', f'Будильник отключен')

root = Tk()
root.geometry('450x250+400+200')
root.title('Будильник')
root.config(bg='black')

time = Label(root, text='00:00:00')
time.config(bg='black', fg='lime', font='Arial 50')
time.pack(pady=10)

alarm = Entry(root)
alarm.config(width=10, justify='center')
alarm['font'] = 'Arial 20'
alarm.pack()

btn_on = Button(root)
btn_on.config(text='Включить', width=10, font='Arial 12', command=start)
btn_on.pack(pady=10)

btn_off = Button(root)
btn_off.config(text='Выключить', width=10, font='Arial 12', command=stop)
btn_off.pack()

alarm_time = ""

def tick():
    global alarm_time
    time_now = strftime('%H:%M:%S')   #strftime('%X')
    #time.config(text=time_now)
    if (alarm_time == time_now or alarm_time == strftime('%H:%M')
            or alarm_time == strftime('%H')):
        alarm_time = " "
        pg.mixer.music.play()
    time['text'] = time_now #виджет описан словарем
    time.after(1000, tick)
tick()

root.mainloop()

