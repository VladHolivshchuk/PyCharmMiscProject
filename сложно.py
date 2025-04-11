# import random as r
#
# class Character:
#     def __init__(self, name, health):
#         self.__name = name
#         self.__health = max(0, health)
#
#     def get_name(self):
#         return self.__name
#
#     def get_health(self):
#         return self.__health
#
#     def take_damage(self, amount):
#         damage = r.randint(1, amount)
#         self.__health = max(0, self.__health - damage)
#         print(f"{self.__name} втрачає {damage} HP!")
#
#     def is_alive(self):
#         return self.__health > 0
#
#     def attack(self, target):
#         pass
#
#     def __str__(self):
#         return f"{self.__name} | HP: {self.__health}"
#
# class Warrior(Character):
#     def __init__(self, name):
#         super().__init__(name, 120)
#
#     def attack(self, target):
#         print(f"{self.get_name()} атакує мечем {target.get_name()}!")
#         target.take_damage(20)
#
# class Mag(Character):
#     def __init__(self, name):
#         super().__init__(name, 70)
#
#     def attack(self, target):
#         print(f"{self.get_name()} кидає магічне закляття на {target.get_name()}!")
#         target.take_damage(25)

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title = title
        self.__author = author
        self.__item_id = item_id
        self._available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_item_id(self):
        return self.__item_id

    def is_same_item(self, other):
        return self.__item_id == other.get_item_id()

    def borrow_item(self):
        if self._available:
            self._available = False
            print(f"Ви взяли: {self.__title}")
        else:
            print("Цей матеріал уже взято!")

    def return_item(self):
        self._available = True
        print(f"Матеріал повернено: {self.__title}")

    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages = pages

    def display_info(self):
        print(f"Книга: {self.get_title()}, Автор: {self.get_author()}, Сторінки: {self.__pages}")

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self.get_title()}, Автор: {self.get_author()}, Номер випуску: {self.__issue_number}")

class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration = duration

    def display_info(self):
        print(f"Аудіокнига: {self.get_title()}, Автор: {self.get_author()}, Тривалість: {self.__duration} хвилин")


items = [
    Book("ТРУ КНИГА ПРО МАГИЮ", "ДАМБЛДОР", 1, 777),
    Magazine("Наука і життя", "Наша биологичка", 2, 42),
    Audiobook("Улица Сталеваров", "Юрий Каплан", 3, 3)
]

for item in items:
    item.display_info()
    item.borrow_item()
    item.return_item()