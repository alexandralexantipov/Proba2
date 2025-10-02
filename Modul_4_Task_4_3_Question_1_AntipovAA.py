# ВАРИАНТ № 1 (чтение файла Demo.log с автоматическим закрытием)
with open('Demo.log', 'r', encoding='utf-8') as file:  # with - файл откроется и закроется сам (даже с ошибкой). Сохраняем файл Demo.log в переменную file в виде объекта. 'r' означает read (чтение) и файл открыт только для чтения.
    s = file.readlines()  # Сохраняем всё в список переменной s, где readlines() - считывает все строки из файла (объекта file)

nec_counter = 0        # Счетчик для NEC (начинает считать с нуля)
sharp_counter = 0      # Счетчик для SHARP (начинает считать с нуля)
sony_counter = 0       # Счетчик для SONY (начинает считать с нуля)

for d in s:  # Переменная d содержит текущую строку, проверяем каждую строку из списка s
    if 'Protocol=NEC' in d:  # Если в строке есть NEC - увеличиваем счетчик NEC на +1
        nec_counter += 1
    elif 'Protocol=SHARP' in d:  # Если в строке есть SHARP - увеличиваем счетчик SHARP на +1
        sharp_counter += 1
    elif 'Protocol=SONY' in d:  # Если в строке есть SONY - увеличиваем счетчик SONY на +1
        sony_counter += 1

print(f"NEC: {nec_counter}\nSHARP: {sharp_counter}\nSONY: {sony_counter}\n")  # Выводим результаты подсчета всех протоколов при помощи f-строки, которая позволяет вставлять значения переменных прямо в текст, \n - перенос строки

# ВАРИАНТ № 2 (с ручным закрытием файла)
s = open('Demo.log', 'r', encoding='utf-8')  # Cохраняем объект в s, открываем файл Demo.log, 'r' означает read (чтение) и файл открыт только для чтения.
z = s.readlines()  # readlines() всегда возвращает список строк из файла, значит z автоматически становится списком

nec, sharp, sony = 0, 0, 0  # Множественное присваивание: слева переменные, справа значения переменных

for d in z:  # Перебираем каждую строку из списка (d - текущая строка)
    if 'Protocol=NEC' in d:    # Если находим NEC
        nec += 1               # Увеличиваем счетчик NEC на 1 (+1)
    elif 'Protocol=SHARP' in d:  # Иначе находим SHARP
        sharp += 1             # Увеличиваем счетчик SHARP на 1 (+1)
    elif 'Protocol=SONY' in d:   # Иначе находим SONY
        sony += 1              # Увеличиваем счетчик SONY на 1 (+1)

print(f"NEC: {nec}\nSHARP: {sharp}\nSONY: {sony}\n") # Выводим финальные результаты подсчета
s.close()  # Закрываем файл Demo.log

# ВАРИАНТ № 3 (Все счетчики в одном словаре)
protocol_counters = {  # Создаем словарь {} для всех счетчиков
    'nec': 0,    # Здесь будет число для NEC
    'sharp': 0,  # Здесь будет число для SHARP
    'sony': 0    # Здесь будет число для SONY
}

for i in open('Demo.log', 'r', encoding='utf-8'):  # Читаем файл построчно (i - текущая строка файла), 'r' означает read (чтение) и файл открыт только для чтения.
    if 'Protocol=NEC' in i:  # Если находим NEC в строке
        protocol_counters['nec'] += 1    # Добавляем 1 к счетчику NEC
    elif 'Protocol=SHARP' in i:   # Иначе находим SHARP в строке
        protocol_counters['sharp'] += 1  # Добавляем 1 к счетчику SHARP
    elif 'Protocol=SONY' in i:    # Иначе находим SONY в строке
        protocol_counters['sony'] += 1   # Добавляем 1 к счетчику SONY

print(f"NEC: {protocol_counters['nec']}\nSHARP: {protocol_counters['sharp']}\nSONY: {protocol_counters['sony']}\n")  # Выводим результаты из словаря protocol_counters, protocol_counters['nec'] - получаем значение по ключу 'nec' из словаря, \n перенос строки

# ВАРИАНТ № 4 (чтение файла в цикле)
nec = 0    # Счетчик для NEC (начинает считать с нуля)
sharp = 0  # Счетчик для SHARP (начинает считать с нуля)
sony = 0   # Счетчик для SONY (начинает считать с нуля)

for i in open('Demo.log', 'r', encoding='utf-8'):  # Файл открывается непосредственно в цикле for (i - текущая строка файла) перебираем все строки, 'r' означает read (чтение) и файл открыт только для чтения.
    if 'Protocol=NEC' in i:      # Проверяем есть ли Protocol=NEC в строке
        nec += 1                 # Если есть - прибавляем 1 к NEC
    elif 'Protocol=SHARP' in i:  # Проверяем есть ли Protocol=SHARP в строке
        sharp += 1               # Если есть - прибавляем 1 к SHARP
    elif 'Protocol=SONY' in i:   # Проверяем есть ли Protocol=SONY в строке
        sony += 1                # Если есть - прибавляем 1 к SONY

print(f"NEC: {nec}\nSHARP: {sharp}\nSONY: {sony}")  # При помощи f строки выводим результаты переменных (в фигурных скобках - {nec},{sharp},{sony}) где подставляется текущее значение переменной
