import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime
import threading
import time


class CryptoCurrencyTracker:
    """
    Класс для создания приложения отслеживания курсов криптовалют
    Использует API CoinGecko для получения данных
    """

    def __init__(self, root):
        """
        Инициализация главного окна приложения

        Args:
            root: Главное окно Tkinter
        """
        self.root = root
        self.root.title("Трекер курсов криптовалют v2.0")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f0f0')

        # Список популярных криптовалют для отслеживания
        self.crypto_list = [
            "bitcoin", "ethereum", "ripple", "cardano",
            "dogecoin", "solana", "polkadot", "litecoin",
            "chainlink", "stellar", "bitcoin-cash", "monero"
        ]

        # Словарь для хранения последних полученных данных
        self.current_data = []

        # Флаг для отслеживания состояния обновления
        self.is_loading = False

        self.setup_ui()
        self.load_data()

        # Запуск автообновления в отдельном потоке
        self.auto_update_thread = threading.Thread(target=self.auto_update, daemon=True)
        self.auto_update_thread.start()

    def setup_ui(self):
        """Настройка графического интерфейса пользователя"""
        # Стилизация
        self.setup_styles()

        # Главный фрейм
        main_frame = ttk.Frame(self.root, padding="15", style='Main.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Заголовок
        title_label = ttk.Label(main_frame,
                                text="📊 Трекер курсов криптовалют",
                                font=("Arial", 18, "bold"),
                                style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=5, pady=(0, 20))

        # Панель управления
        control_frame = ttk.Frame(main_frame, style='Control.TFrame')
        control_frame.grid(row=1, column=0, columnspan=5, sticky=(tk.W, tk.E), pady=(0, 15))

        # Кнопка обновления
        self.refresh_btn = ttk.Button(control_frame,
                                      text="🔄 Обновить данные",
                                      command=self.load_data,
                                      style='Accent.TButton')
        self.refresh_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Индикатор загрузки
        self.loading_label = ttk.Label(control_frame,
                                       text="",
                                       font=("Arial", 10),
                                       style='Status.TLabel')
        self.loading_label.pack(side=tk.LEFT)

        # Статистика
        self.stats_label = ttk.Label(control_frame,
                                     text="Криптовалют: 0",
                                     style='Stats.TLabel')
        self.stats_label.pack(side=tk.RIGHT)

        # Таблица для отображения данных
        self.setup_table(main_frame)

        # Статус-бар
        self.setup_status_bar(main_frame)

        # Настройка адаптивного layout
        self.setup_layout(main_frame)

    def setup_styles(self):
        """Настройка стилей элементов интерфейса"""
        style = ttk.Style()
        style.configure('Main.TFrame', background='#f0f0f0')
        style.configure('Control.TFrame', background='#e0e0e0')
        style.configure('Title.TLabel', background='#f0f0f0', foreground='#2c3e50')
        style.configure('Status.TLabel', background='#e0e0e0', foreground='#7f8c8d')
        style.configure('Stats.TLabel', background='#e0e0e0', foreground='#34495e')
        style.configure('Accent.TButton', font=('Arial', 10, 'bold'))

        # Стили для таблицы
        style.configure('Treeview',
                        font=('Arial', 10),
                        rowheight=25)
        style.configure('Treeview.Heading',
                        font=('Arial', 11, 'bold'),
                        background='#34495e',
                        foreground='white')

    def setup_table(self, parent):
        """Настройка таблицы для отображения данных о криптовалютах"""
        # Создание Treeview с колонками
        columns = ("rank", "name", "symbol", "price", "change_24h", "market_cap")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=16)

        # Настройка колонок
        columns_config = [
            ("rank", "№", 50),
            ("name", "Название криптовалюты", 200),
            ("symbol", "Символ", 100),
            ("price", "Цена (USD)", 150),
            ("change_24h", "Изменение за 24ч (%)", 150),
            ("market_cap", "Капитализация", 150)
        ]

        for col_id, heading, width in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor=tk.CENTER)

        self.tree.grid(row=2, column=0, columnspan=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Полоса прокрутки для таблицы
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=2, column=5, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Привязка события двойного клика
        self.tree.bind("<Double-1>", self.on_item_double_click)

    def setup_status_bar(self, parent):
        """Настройка статус-бара"""
        status_frame = ttk.Frame(parent, style='Control.TFrame')
        status_frame.grid(row=3, column=0, columnspan=5, sticky=(tk.W, tk.E), pady=(15, 0))

        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе...")

        status_label = ttk.Label(status_frame,
                                 textvariable=self.status_var,
                                 style='Status.TLabel')
        status_label.pack(side=tk.LEFT, padx=5)

        # Время последнего обновления
        self.last_update_var = tk.StringVar()
        self.last_update_var.set("Последнее обновление: --:--:--")

        update_label = ttk.Label(status_frame,
                                 textvariable=self.last_update_var,
                                 style='Status.TLabel')
        update_label.pack(side=tk.RIGHT, padx=5)

    def setup_layout(self, parent):
        """Настройка адаптивного расположения элементов"""
        # Настройка весов для растягивания
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(2, weight=1)

    def fetch_crypto_data(self):
        """
        Получение данных с API CoinGecko

        Returns:
            list|None: Список данных о криптовалютах или None при ошибке
        """
        try:
            self.status_var.set("Подключение к API...")

            url = "https://api.coingecko.com/api/v3/coins/markets"
            params = {
                'vs_currency': 'usd',
                'ids': ','.join(self.crypto_list),
                'order': 'market_cap_desc',
                'per_page': len(self.crypto_list),
                'page': 1,
                'sparkline': False,
                'price_change_percentage': '24h'
            }

            # Выполнение HTTP-запроса с таймаутом
            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()  # Проверка HTTP ошибок

            # Парсинг JSON данных
            data = response.json()
            self.status_var.set("Данные успешно получены")

            return data

        except requests.exceptions.Timeout:
            messagebox.showerror("Ошибка", "Таймаут соединения с API")
            return None
        except requests.exceptions.ConnectionError:
            messagebox.showerror("Ошибка", "Проверьте подключение к интернету")
            return None
        except requests.exceptions.HTTPError as e:
            messagebox.showerror("Ошибка API", f"HTTP ошибка: {e}")
            return None
        except json.JSONDecodeError as e:
            messagebox.showerror("Ошибка данных", f"Ошибка парсинга JSON: {e}")
            return None
        except Exception as e:
            messagebox.showerror("Неизвестная ошибка", f"Произошла ошибка: {e}")
            return None

    def load_data(self):
        """Запуск загрузки данных с обработкой состояния интерфейса"""
        if self.is_loading:
            return

        self.is_loading = True
        self.refresh_btn.config(state="disabled")
        self.loading_label.config(text="Загрузка...")

        # Запуск в отдельном потоке
        thread = threading.Thread(target=self._load_data_thread)
        thread.daemon = True
        thread.start()

    def _load_data_thread(self):
        """Поток для загрузки данных"""
        data = self.fetch_crypto_data()
        self.root.after(0, self._update_display, data)

    def _update_display(self, data):
        """Обновление отображения данных в главном потоке"""
        # Очистка таблицы
        for item in self.tree.get_children():
            self.tree.delete(item)

        if data and isinstance(data, list):
            self.current_data = data

            # Сортировка по рыночной капитализации
            sorted_data = sorted(data, key=lambda x: x.get('market_cap', 0), reverse=True)

            for index, crypto in enumerate(sorted_data, 1):
                self.add_crypto_to_table(index, crypto)

            # Обновление статистики
            self.stats_label.config(text=f"Криптовалют: {len(sorted_data)}")
            self.last_update_var.set(f"Последнее обновление: {datetime.now().strftime('%H:%M:%S')}")

            self.status_var.set("Данные успешно загружены")
        else:
            self.status_var.set("Ошибка загрузки данных")
            messagebox.showwarning("Внимание", "Не удалось получить данные")

        # Сброс состояния интерфейса
        self.is_loading = False
        self.refresh_btn.config(state="normal")
        self.loading_label.config(text="")

    def add_crypto_to_table(self, rank, crypto):
        """Добавление данных о криптовалюте в таблицу"""
        try:
            name = crypto.get('name', 'N/A')
            symbol = crypto.get('symbol', '').upper()
            price = crypto.get('current_price', 0)
            change_24h = crypto.get('price_change_percentage_24h', 0)
            market_cap = crypto.get('market_cap', 0)

            # Форматирование значений
            price_str = self.format_price(price)
            change_str = f"{change_24h:+.2f}%"
            market_cap_str = self.format_market_cap(market_cap)

            # Вставка данных
            item_id = self.tree.insert("", tk.END, values=(
                rank, name, symbol, price_str, change_str, market_cap_str
            ))

            # Цветовая индикация
            if change_24h > 0:
                self.tree.set(item_id, "change_24h", f"▲ {change_str}")
                self.tree.item(item_id, tags=('positive',))
            elif change_24h < 0:
                self.tree.set(item_id, "change_24h", f"▼ {change_str}")
                self.tree.item(item_id, tags=('negative',))

            # Настройка тегов для цветов
            self.tree.tag_configure('positive', foreground='#27ae60')  # Зеленый
            self.tree.tag_configure('negative', foreground='#e74c3c')  # Красный

        except Exception as e:
            print(f"Ошибка добавления данных: {e}")

    def format_price(self, price):
        """Форматирование цены для отображения"""
        if price >= 1000:
            return f"${price:,.2f}"
        elif price >= 1:
            return f"${price:.2f}"
        elif price >= 0.01:
            return f"${price:.4f}"
        else:
            return f"${price:.6f}"

    def format_market_cap(self, market_cap):
        """Форматирование рыночной капитализации"""
        if market_cap >= 1e12:  # Триллионы
            return f"${market_cap / 1e12:.2f}T"
        elif market_cap >= 1e9:  # Миллиарды
            return f"${market_cap / 1e9:.2f}B"
        elif market_cap >= 1e6:  # Миллионы
            return f"${market_cap / 1e6:.2f}M"
        else:
            return f"${market_cap:,.0f}"

    def on_item_double_click(self, event):
        """Обработчик двойного клика по элементу таблицы"""
        item = self.tree.selection()[0] if self.tree.selection() else None
        if item:
            values = self.tree.item(item, 'values')
            messagebox.showinfo("Информация", f"Вы выбрали: {values[1]} ({values[2]})")

    def auto_update(self):
        """Автоматическое обновление данных каждые 60 секунд"""
        while True:
            time.sleep(60)
            if self.root.winfo_exists() and not self.is_loading:
                self.root.after(0, self.load_data)

    def run(self):
        """Запуск главного цикла приложения"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.root.quit()
        except Exception as e:
            messagebox.showerror("Критическая ошибка", f"Приложение завершено с ошибкой: {e}")


def main():
    """
    Главная функция приложения
    Обеспечивает корректный запуск и обработку исключений
    """
    try:
        # Создание главного окна
        root = tk.Tk()

        # Создание и запуск приложения
        app = CryptoCurrencyTracker(root)

        # Центрирование окна на экране
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        app.run()

    except ImportError as e:
        print(f"Ошибка импорта модулей: {e}")
        print("Убедитесь, что установлены все зависимости: pip install requests")
    except Exception as e:
        messagebox.showerror("Ошибка запуска", f"Не удалось запустить приложение: {e}")


# Точка входа в программу
if __name__ == "__main__":
    main()