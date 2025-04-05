class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        print("Товар:", self.name, "Ціна:", self.price, "Кількість:", self.quantity)


class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)
        print("Додано:", product.name)

    def show(self):
        print("У кошику:")
        total = 0
        for item in self.items:
            item.__str__()
            total += item.price
        print("Загальна вартість:", total)

    def remove(self, product_name):
        for i in range(len(self.items)):
            if self.items[i].name == product_name:
                del self.items[i]
                print("Видалено:", product_name)
                break
                #чистосердечное признание, эту часть я написал с гпт т.к не совсем понял как сделать удаление предмета


p1 = Product("ПК", 12000, 2)
p2 = Product("Хлеб", 122, 5)

cart = Cart()
cart.add(p1)
cart.add(p2)
cart.show()
cart.remove("Хлеб")
cart.show()


