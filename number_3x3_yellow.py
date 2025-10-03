import tkinter as tk
from tkinter import ttk


class ButtonGrid:
    def __init__(self, root):
        self.root = root
        self.root.title("Квадрат 3x3")
        self.root.configure(bg='lightgray')

        # Центрирование окна на экране (уменьшил размер окна)
        self.center_window(300, 300)

        # Создание основного фрейма
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Создание кнопок 3x3
        self.buttons = []
        self.button_states = {}  # Словарь для отслеживания состояний кнопок
        self.create_buttons(main_frame)

        # Настройка расширяемости
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure((0, 1, 2), weight=1)
        main_frame.rowconfigure((0, 1, 2), weight=1)

    def center_window(self, width, height):
        """Центрирует окно на экране"""
        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Вычисляем координаты для центрирования
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Устанавливаем положение и размер окна
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def create_buttons(self, parent):
        """Создает компактную сетку кнопок 3x3"""
        for row in range(3):
            for col in range(3):
                # Вычисляем номер кнопки
                button_number = row * 3 + col + 1

                # Создаем компактную кнопку
                button = tk.Button(
                    parent,
                    text=str(button_number),
                    font=('Arial', 12, 'bold'),  # Уменьшил шрифт
                    width=4,  # Уменьшил ширину
                    height=2,  # Уменьшил высоту
                    bg='gray',  # Серый цвет по умолчанию
                    fg='white',  # Белый текст
                    activebackground='darkgray',
                    relief='raised',
                    bd=2,  # Уменьшил границу
                    command=lambda num=button_number: self.button_click(num)
                )

                # Размещаем кнопку в сетке с меньшими отступами
                button.grid(
                    row=row,
                    column=col,
                    padx=2,  # Уменьшил отступы
                    pady=2,
                    sticky=(tk.W, tk.E, tk.N, tk.S)
                )

                self.buttons.append(button)
                # Изначально все кнопки не активны (серые)
                self.button_states[button_number] = False

    def button_click(self, button_number):
        """Обработчик нажатия кнопки"""
        # Меняем состояние кнопки
        self.button_states[button_number] = not self.button_states[button_number]

        # Меняем цвет кнопки в зависимости от состояния
        if self.button_states[button_number]:
            # Делаем кнопку желтой
            self.buttons[button_number - 1].configure(
                bg='yellow',
                fg='black'
            )
        else:
            # Возвращаем серый цвет
            self.buttons[button_number - 1].configure(
                bg='gray',
                fg='white'
            )

        print(f"Кнопка {button_number}: {'желтая' if self.button_states[button_number] else 'серая'}")


def main():
    # Создаем главное окно
    root = tk.Tk()

    # Создаем и запускаем приложение
    app = ButtonGrid(root)

    # Запускаем главный цикл
    root.mainloop()


if __name__ == "__main__":
    main()