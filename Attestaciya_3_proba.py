import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime
import threading
import time


class CryptoCurrencyViewer:
    """
    Класс для создания приложения отображения курсов криптовалют
    Использует API Binance для получения данных
    """

    def __init__(self, root):
        """
        Инициализация главного окна приложения
        """
        self.root = root
        self.root.title("Монитор курсов криптовалют - Binance")
        self.root.geometry("900x650")
        self.root.resizable(True, True)
        self.root.configure(bg='#f0f0f0')

        # Список криптовалют для отображения (пара к USDT)
        self.crypto_pairs = [
            "BTCUSDT", "ETHUSDT", "XRPUSDT", "ADAUSDT",
            "DOGEUSDT", "SOLUSDT", "DOTUSDT", "LTCUSDT",
            "LINKUSDT", "XLMUSDT", "BCHUSDT", "XMRUSDT"
        ]

        # Словарь для понятных названий криптовалют
        self.crypto_names = {
            "BTCUSDT": "Bitcoin",
            "ETHUSDT": "Ethereum",
            "XRPUSDT": "Ripple",
            "ADAUSDT": "Cardano",
            "DOGEUSDT": "Dogecoin",
            "SOLUSDT": "Solana",
            "DOTUSDT": "Polkadot",
            "LTCUSDT": "Litecoin",
            "LINKUSDT": "Chainlink",
            "XLMUSDT": "Stellar",
            "BCHUSDT": "Bitcoin Cash",
            "XMRUSDT": "Monero"
        }

        self.current_data = []
        self.is_loading = False

        self.setup_ui()
        self.load_data()

        # Запуск автообновления
        self.auto_update_thread = threading.Thread(target=self.auto_update, daemon=True)
        self.auto_update_thread.start()

    def fetch_binance_data(self):
        """
        Получение данных с API Binance
        """
        try:
            self.status_var.set("Загрузка данных с Binance...")

            all_data = []

            for pair in self.crypto_pairs:
                # URL для получения текущей цены
                price_url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"

                # URL для получения статистики за 24 часа
                stats_url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={pair}"

                price_response = requests.get(price_url, timeout=10)
                stats_response = requests.get(stats_url, timeout=10)

                price_response.raise_for_status()
                stats_response.raise_for_status()

                price_data = price_response.json()
                stats_data = stats_response.json()

                crypto_data = {
                    'symbol': pair,
                    'name': self.crypto_names.get(pair, pair),
                    'price': float(price_data['price']),
                    'price_change_percent': float(stats_data['priceChangePercent']),
                    'volume': float(stats_data['volume']),
                    'high_price': float(stats_data['highPrice']),
                    'low_price': float(stats_data['lowPrice'])
                }

                all_data.append(crypto_data)

            self.status_var.set("Данные с Binance успешно загружены")
            return all_data

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Ошибка сети", f"Ошибка подключения к Binance: {e}")
            return None
        except json.JSONDecodeError as e:
            messagebox.showerror("Ошибка данных", f"Ошибка обработки данных: {e}")
            return None
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неизвестная ошибка: {e}")
            return None

    def setup_ui(self):
        """Настройка графического интерфейса"""
        # Стилизация
        self.setup_styles()

        # Главный фрейм
        main_frame = ttk.Frame(self.root, padding="15", style='Main.TFrame')
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Заголовок с указанием источника данных
        title_label = ttk.Label(main_frame,
                                text="📊 Курсы криптовалют (данные: Binance)",
                                font=("Arial", 16, "bold"),
                                style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=6, pady=(0, 20))

        # Панель управления
        control_frame = ttk.Frame(main_frame, style='Control.TFrame')
        control_frame.grid(row=1, column=0, columnspan=6, sticky=(tk.W, tk.E), pady=(0, 15))

        self.refresh_btn = ttk.Button(control_frame,
                                      text="🔄 Обновить",
                                      command=self.load_data,
                                      style='Accent.TButton')
        self.refresh_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.loading_label = ttk.Label(control_frame, text="", style='Status.TLabel')
        self.loading_label.pack(side=tk.LEFT)

        self.stats_label = ttk.Label(control_frame, text="Криптовалют: 0", style='Stats.TLabel')
        self.stats_label.pack(side=tk.RIGHT)

        # Таблица
        self.setup_table(main_frame)

        # Статус-бар
        self.setup_status_bar(main_frame)
        self.setup_layout(main_frame)

    def setup_table(self, parent):
        """Настройка таблицы с дополнительными колонками"""
        columns = ("rank", "name", "symbol", "price", "change_24h", "high", "low", "volume")
        self.tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)

        columns_config = [
            ("rank", "№", 40),
            ("name", "Название", 120),
            ("symbol", "Пара", 80),
            ("price", "Цена (USDT)", 100),
            ("change_24h", "Изменение 24ч", 100),
            ("high", "Макс цена", 100),
            ("low", "Мин цена", 100),
            ("volume", "Объем торгов", 120)
        ]

        for col_id, heading, width in columns_config:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor=tk.CENTER)

        self.tree.grid(row=2, column=0, columnspan=6, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=2, column=6, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)

    def setup_styles(self):
        """Настройка стилей"""
        style = ttk.Style()
        style.configure('Main.TFrame', background='#f0f0f0')
        style.configure('Control.TFrame', background='#e0e0e0')
        style.configure('Title.TLabel', background='#f0f0f0', foreground='#2c3e50')
        style.configure('Status.TLabel', background='#e0e0e0')
        style.configure('Stats.TLabel', background='#e0e0e0')
        style.configure('Accent.TButton', font=('Arial', 10, 'bold'))
        style.configure('Treeview', font=('Arial', 9))
        style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

    def setup_status_bar(self, parent):
        """Настройка статус-бара"""
        status_frame = ttk.Frame(parent, style='Control.TFrame')
        status_frame.grid(row=3, column=0, columnspan=6, sticky=(tk.W, tk.E), pady=(15, 0))

        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе с Binance API...")

        status_label = ttk.Label(status_frame, textvariable=self.status_var, style='Status.TLabel')
        status_label.pack(side=tk.LEFT, padx=5)

        self.last_update_var = tk.StringVar()
        self.last_update_var.set("Обновление: --:--:--")

        update_label = ttk.Label(status_frame, textvariable=self.last_update_var, style='Status.TLabel')
        update_label.pack(side=tk.RIGHT, padx=5)

    def setup_layout(self, parent):
        """Настройка layout"""
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(2, weight=1)

    def load_data(self):
        """Загрузка данных"""
        if self.is_loading:
            return

        self.is_loading = True
        self.refresh_btn.config(state="disabled")
        self.loading_label.config(text="Загрузка с Binance...")

        thread = threading.Thread(target=self._load_data_thread)
        thread.daemon = True
        thread.start()

    def _load_data_thread(self):
        """Поток загрузки данных"""
        data = self.fetch_binance_data()
        self.root.after(0, self._update_display, data)

    def _update_display(self, data):
        """Обновление отображения"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        if data:
            self.current_data = data

            for index, crypto in enumerate(data, 1):
                self.add_crypto_to_table(index, crypto)

            self.stats_label.config(text=f"Криптовалют: {len(data)}")
            self.last_update_var.set(f"Обновлено: {datetime.now().strftime('%H:%M:%S')}")
            self.status_var.set("Данные актуальны")
        else:
            self.status_var.set("Ошибка загрузки")

        self.is_loading = False
        self.refresh_btn.config(state="normal")
        self.loading_label.config(text="")

    def add_crypto_to_table(self, rank, crypto):
        """Добавление криптовалюты в таблицу"""
        try:
            symbol_clean = crypto['symbol'].replace('USDT', '')

            values = (
                rank,
                crypto['name'],
                symbol_clean,
                f"${crypto['price']:,.2f}",
                f"{crypto['price_change_percent']:+.2f}%",
                f"${crypto['high_price']:,.2f}",
                f"${crypto['low_price']:,.2f}",
                f"{crypto['volume']:,.0f}"
            )

            item_id = self.tree.insert("", tk.END, values=values)

            # Цветовая индикация
            if crypto['price_change_percent'] > 0:
                self.tree.item(item_id, tags=('positive',))
            else:
                self.tree.item(item_id, tags=('negative',))

            self.tree.tag_configure('positive', foreground='#27ae60')
            self.tree.tag_configure('negative', foreground='#e74c3c')

        except Exception as e:
            print(f"Ошибка добавления: {e}")

    def auto_update(self):
        """Автообновление каждые 30 секунд"""
        while True:
            time.sleep(30)
            if self.root.winfo_exists() and not self.is_loading:
                self.root.after(0, self.load_data)

    def run(self):
        """Запуск приложения"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка приложения: {e}")


def main():
    """
    Главная функция приложения с данными от Binance
    """
    try:
        root = tk.Tk()
        app = CryptoCurrencyViewer(root)

        # Центрирование окна
        root.update_idletasks()
        x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
        y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
        root.geometry(f"+{x}+{y}")

        app.run()

    except ImportError as e:
        print(f"Ошибка: {e}")
        print("Установите зависимости: pip install requests")
    except Exception as e:
        messagebox.showerror("Ошибка запуска", f"Ошибка: {e}")


if __name__ == "__main__":
    main()