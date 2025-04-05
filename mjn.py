# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         print("Товар:", self.name, "Ціна:", self.price, "Кількість:", self.quantity)
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add(self, product):
#         self.items.append(product)
#         print("Додано:", product.name)
#
#     def show(self):
#         print("У кошику:")
#         total = 0
#         for item in self.items:
#             item.__str__()
#             total += item.price
#         print("Загальна вартість:", total)
#
#     def remove(self, product_name):
#         for i in range(len(self.items)):
#             if self.items[i].name == product_name:
#                 del self.items[i]
#                 print("Видалено:", product_name)
#                 break
#                 #чистосердечное признание, эту часть я написал с гпт т.к не совсем понял как сделать удаление предмета
#
#
# p1 = Product("ПК", 12000, 2)
# p2 = Product("Хлеб", 122, 5)
#
# cart = Cart()
# cart.add(p1)
# cart.add(p2)
# cart.show()
# cart.remove("Хлеб")
# cart.show()

#2

class BankAccount:
    def __init__(self, owner, number, balance):
        self.owner = owner
        self.number = number
        self.balance = balance

    def __str__(self):
        print("Власник:", self.owner, "Рахунок:", self.number, "Баланс:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Поповнення:", amount, "Новий баланс:", self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Знято:", amount, "Залишок:", self.balance)
        else:
            print("Недостатньо коштів")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)

    def transfer(self, from_acc, to_acc, amount):
        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print("Переказ:", amount, "від", from_acc.owner, "до", to_acc.owner)

a1 = BankAccount("вАЛЯ", "998", 1000)
a2 = BankAccount("Женя", "21", 510)

bank = Bank()
bank.add_account(a1)
bank.add_account(a2)

a1.__str__()
a2.__str__()

bank.transfer(a1, a2, 300)

a1.__str__()
a2.__str__()





