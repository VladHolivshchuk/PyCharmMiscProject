
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

class Pay:
    def process(self,money):
        pass
class Credit(Pay):
    def process(self, money):
        return 'Оплата ' + str(money)+ " грн карткою"
class Cash(Pay):
    def process(self, money):
        return "Оплата " + str(money)+ " грн готівкою"
class System(Pay):
    def process(self, money):
        return "Оплата "+str(money)+" грн онлайн"

buy=(Credit(),Cash(),System())
for i in buy:
    print(i.process(123))
print()