# def pok(tvar):
#     print(tvar.info())
#
# class Tvar:
#     def info(self):
#         return "тварина"
#
# class Sobaka(Tvar):
#     def info(self):
#         return "собака"
#
# class Kit(Tvar):
#     def info(self):
#         return "кіт"
#
#
#
# t1 = Sobaka()
# t2 = Kit()
# pok(t1)
# pok(t2)




class Transport:
    def speed(self):
        return "Шв не вказана"

    def move(self):
        return "Рухається"

class Avto(Transport):
    def speed(self):
        return super().speed() + "авто може їхати 100 км/год"

class Velyk(Transport):
    def speed(self):
        return super().speed() + "велосипед їде 20 км/год"

def info_speed(t):
    print(t.speed())
    print(t.move())

a = Avto()
v = Velyk()
info_speed(a)
info_speed(v)