import requests
import re
from bs4 import BeautifulSoup as bs

class Coin:
    def __init__(self, url):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        self.soup = None
        self.coins_data = []

    def auditSite(self):
        try:
            response = requests.get(self.url, headers=self.header, timeout=10)
            response.raise_for_status()
            self.soup = bs(response.text, "html.parser")
            print("Успішно підключено до {}. Статус: {}".format(self.url, response.status_code))
            return True
        except requests.exceptions.RequestException as e:
            print("Не вдалося підключитися до сайту {}. Помилка: {}".format(self.url, e))
            return False
        except Exception as e:
            print("Виникла інша помилка при доступі до сайту: {}".format(e))
            return False

    def getInfo(self):
        if not self.soup:
            print("Помилка: об'єкт BeautifulSoup не ініціалізовано. Запустіть auditSite() спочатку.")
            return []

        coins = []
        table = self.soup.find('table', class_='cmc-table')
        if not table:
            print("Помилка: не знайдено таблицю криптовалют на сторінці.")
            return coins
        listCoin = table.find('tbody')
        if not listCoin:
            print("Помилка: не знайдено тіло таблиці ('tbody').")
            return coins

        try:
            info = listCoin.find_all('tr')[0:10]
        except Exception as e:
            print("Помилка при пошуку рядків ('tr') у таблиці: {}".format(e))
            return coins

        for i in info:
            name_cell = i.select_one('td:nth-of-type(3) p')
            name2 = name_cell.text.strip() if name_cell else 'Відсутня назва'

            price_cell = i.select_one('td:nth-of-type(4) span')
            price2 = price_cell.text.strip() if price_cell else "Відсутня ціна"

            coins.append({
                "Назва": name2,
                "Ціна": price2,
            })

        self.coins_data = coins
        return coins

    def showInfo(self, coins):
        if not coins:
            print("Немає даних для відображення.")
            return

        print()
        print("\tТОП-10 КРИПТОВАЛЮТ")
        print("{:<4}{:<25}{:<20}".format('№', 'НАЗВА', 'ЦІНА'))
        num = 1
        for i in coins:
            name_display = (i['Назва'][:22] + '...') if len(i['Назва']) > 22 else i['Назва']
            print("{:<4}{:<25}{:<20}".format(num, name_display, i['Ціна']))
            num += 1
        print()

def clean_price(price_str):
    if isinstance(price_str, str):
        cleaned = re.sub(r'[$,]', '', price_str)
        try:
            return float(cleaned)
        except ValueError:
            return 0.0
    return 0.0

url = "https://coinmarketcap.com/"
obj = Coin(url)

if obj.auditSite():
    site_data = obj.getInfo()

    if site_data:
        obj.showInfo(site_data)

        order = []
        total_cost = 0.0

        while True:
            while True:
                try:
                    item_choice = input("Який товар ви хочете придбати? (введіть номер, 1-10): ")
                    item_index = int(item_choice) - 1
                    if 0 <= item_index < len(obj.coins_data):
                        chosen_product_info = obj.coins_data[item_index]
                        break
                    else:
                        print("Неправильний номер. Введіть число від 1 до {}.".format(len(obj.coins_data)))
                except ValueError:
                    print("Будь ласка, введіть номер товару (число).")

            while True:
                try:
                    quantity_choice = input("Скільки одиниць ви хочете купити?: ")
                    quantity = float(quantity_choice)
                    if quantity > 0:
                        break
                    else:
                        print("Кількість повинна бути більше нуля.")
                except ValueError:
                    print("Будь ласка, введіть кількість товару (число, можливо дробове).")

            raw_price = chosen_product_info.get("Ціна", "0")
            numeric_price = clean_price(raw_price)

            if numeric_price == 0.0:
                 print("Увага: не вдалося визначити ціну для {}. Цей товар не буде додано до замовлення.".format(chosen_product_info['Назва']))
            else:
                order.append({
                    "name": chosen_product_info["Назва"],
                    "quantity": quantity,
                    "price_per_unit": numeric_price
                    })
                print("Додано: {} x{}".format(chosen_product_info['Назва'], quantity))

            while True:
                more_items = input("Хочете ще щось? (так/ні): ").lower().strip()
                if more_items in ["так", "ні", "yes", "no"]:
                    break
                else:
                    print("Будь ласка, введіть 'так' або 'ні'.")

            if more_items in ["ні", "no"]:
                break

        print()
        print("Ваше Замовлення:")
        if not order:
            print("Ваше замовлення порожнє")
        else:
            for item in order:
                subtotal = item["quantity"] * item["price_per_unit"]
                total_cost += subtotal
                # Спрощене виведення ціни та підсумку
                print("{} x {:.4f} (@ ${}) = ${}".format(
                    item['name'],
                    item['quantity'],
                    str(item['price_per_unit']),
                    str(subtotal)
                ))

            print()
            # Спрощене виведення загальної суми
            print("ДДо салти: $" + str(total_cost))
        print()