from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

# Глобальный словарь валют с полными названиями
CURRENCIES = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

def update_base_label(event=None):
    """Обновляет метку с названием базовой валюты"""
    code = base_combobox.get()
    # Используем метод get для избежания ошибки, если код вдруг не найден
    name = CURRENCIES.get(code, "Неизвестная валюта")
    base_label.config(text=name)

def update_target_label(event=None):
    """Обновляет метку с названием целевой валюты"""
    code = target_combobox.get()
    name = CURRENCIES.get(code, "Неизвестная валюта")
    target_label.config(text=name)

def get_exchange_rate():
    """Основная функция для получения и отображения курса обмена"""
    base_code = base_combobox.get()    # Код базовой валюты (из которой конвертируем)
    target_code = target_combobox.get() # Код целевой валюты (в которую конвертируем)

    # Проверка, что пользователь выбрал обе валюты
    if not base_code:
        mb.showwarning("Внимание", "Пожалуйста, выберите базовую валюту.")
        return
    if not target_code:
        mb.showwarning("Внимание", "Пожалуйста, выберите целевую валюту.")
        return

    # Проверка, что базовая и целевая валюта разные
    if base_code == target_code:
        mb.showwarning("Внимание", "Базовая и целевая валюта должны отличаться.")
        return

    try:
        # Выполняем запрос к API, используя выбранную базовую валюту
        response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
        # Генерируем исключение, если запрос завершился с ошибкой (например, 404)
        response.raise_for_status()

        # Парсим JSON-ответ
        data = response.json()

        # Проверяем, что API вернул успешный статус
        if data['result'] == 'success':
            # Проверяем, что целевая валюта есть в списке курсов
            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base_name = CURRENCIES.get(base_code, base_code)
                target_name = CURRENCIES.get(target_code, target_code)

                # Форматируем сообщение. :.2f - округляем до двух знаков после запятой
                result_text = f"1 {base_name} ({base_code}) = {exchange_rate:.2f} {target_name} ({target_code})"
                result_label.config(text=result_text) # Выводим результат в метку

            else:
                mb.showerror("Ошибка", f"Курс для валюты {target_code} не найден.")
        else:
            mb.showerror("Ошибка API", "Не удалось получить данные от сервера.")

    except requests.exceptions.ConnectionError:
        mb.showerror("Ошибка сети", "Проверьте подключение к интернету.")
    except requests.exceptions.RequestException as e:
        mb.showerror("Ошибка запроса", f"Произошла ошибка: {e}")
    except Exception as e:
        mb.showerror("Неизвестная ошибка", f"Произошла непредвиденная ошибка: {e}")

# --- Создание графического интерфейса ---
window = Tk()
window.title("Конвертер валют")
window.geometry("400x300") # Немного увеличим окно для лучшего отображения
window.resizable(False, False) # Запрещаем изменение размера

# Стилизация для улучшения внешнего вида
style = ttk.Style()
style.configure('TLabel', font=('Arial', 10))
style.configure('TButton', font=('Arial', 10, 'bold'))
style.configure('TCombobox', font=('Arial', 10))

# Фрейм для базовой валюты
base_frame = ttk.Frame(window)
base_frame.pack(padx=20, pady=10, fill=X)

ttk.Label(base_frame, text="Базовая валюта:").pack(anchor=W)
base_combobox = ttk.Combobox(base_frame, values=list(CURRENCIES.keys()), state="readonly")
base_combobox.pack(fill=X, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)
base_label = ttk.Label(base_frame, text="Выберите валюту", foreground="gray")
base_label.pack(anchor=W)

# Фрейм для целевой валюты
target_frame = ttk.Frame(window)
target_frame.pack(padx=20, pady=10, fill=X)

ttk.Label(target_frame, text="Целевая валюта:").pack(anchor=W)
target_combobox = ttk.Combobox(target_frame, values=list(CURRENCIES.keys()), state="readonly")
target_combobox.pack(fill=X, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)
target_label = ttk.Label(target_frame, text="Выберите валюту", foreground="gray")
target_label.pack(anchor=W)

# Кнопка для выполнения конвертации
button_frame = ttk.Frame(window)
button_frame.pack(padx=20, pady=20)
convert_button = ttk.Button(button_frame, text="Конвертировать", command=get_exchange_rate)
convert_button.pack()

# Метка для отображения результата
result_frame = ttk.Frame(window)
result_frame.pack(padx=20, pady=10, fill=X)
result_label = ttk.Label(result_frame, text="Здесь будет результат", font=('Arial', 11, 'bold'), wraplength=350)
result_label.pack()

# Запускаем главный цикл обработки событий
window.mainloop()