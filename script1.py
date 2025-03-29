
# class Animal:
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         return "ГАВ"
#
# class Cat(Animal):
#     def sound(self):
#         return "МЯУ"
#
# class Cow(Animal):
#     def sound(self):
#         return "МУ"
# def speak(an):
#     print(an.sound())
#
# a1=Dog()
# a2=Cat()
# a3=Cow()
# speak(a1)
# speak(a2)
# speak(a3)

# class Pay:
#     def process(self,money):
#         pass
# class Credit(Pay):
#     def process(self, money):
#         return 'Оплата ' + str(money)+ " грн карткою"
# class Cash(Pay):
#     def process(self, money):
#         return "Оплата " + str(money)+ " грн готівкою"
# class System(Pay):
#     def process(self, money):
#         return "Оплата "+str(money)+" грн онлайн"
#
# buy=(Credit(),Cash(),System())
# for i in buy:
#     print(i.process(123))
# print()

# import random as r
#
# class Character:
#     def __init__(self, name, health):
#         self.__name = name
#         self.__health = r.randint(0, 100)
#
#     def info_name(self):
#         return self.__name
#
#     def info_hp(self):
#         return self.__health
#
#     def attack(self):
#         pass
#
#     def info_hp(self):
#         return self.__health
#
#     def attack(self):
#         pass
#
#     def take_damage(self, damage):
#         self.__health-=r.randint(0, 10)
#
#     def is_alive(self):
#         return self.__health>0
#     def __str__(self):
#         return self.__name+"my hp:"+str(self.__health)
#
# class Warrior(Character):
#     def __init__(self, name, health):
#         super().__init__(name, health)
#
#     def attack(self,num):
#         print(self.__name + "attacking knight!")
#         num.take_damage(r.randint(1, 6))

sc