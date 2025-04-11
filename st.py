import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10,100)
        self.progress=r.randint(0,10)
        self.alive=True
    def study(self):
        print('Час для навчання')
        self.happy=r.randint(1,50)
        self,progress+=r.randint(1,10)
    def sleep(self):
        print('Час для cну')
        self.happy = r.randint(1, 10)
    def chill(self):
        print('Час для відпочинку')
        self.happy = r.randint(50, 100)
        self, progress += r.randint(5, 10)
    def isAlive(self):
        if 1<self.progress<5:
            print('тебе відчислять, вчись')
            self.alive=False
            elif self.progress <=1
            print('Відчислять з інституту')
            self.alive = False
            elif self.progress >=5:
            print('Добре навчаешься!')
            self.alive = False
        def everyday(self):
            print("Рівень Щастя", self.happy)
            print("Прогрес навчання", self.progress)
        def studyLife(self,day):
            day="День №"+str(day)
            print(day)
            res=r.randint(1,3)
            if res==1
                self.study()
            elif res==2:
                self chill()
            else:
                seld sleep()
            self.everyday()
            self.isAlive()

st1=Student('Олег')
# print(st1.progress)
print("Життя студента",st1.name)
for k in range(7):
    if st1.alive==False:
        break
    st1.studyLife(k)


def study(self):
    print(" Час для навчання")
    self.happy -= r.randint(10, 20)
    self.progress += r.randint(5, 10)
    self.hunger -= r.randint(5, 15)  # Навчання витрачає енергію


def sleep(self):
    print(" Час для сну")
    self.happy += r.randint(5, 15)
    self.health += r.randint(5, 10)
    self.hunger -= r.randint(10, 20)


def chill(self):
    print(" Час для відпочинку")
    self.happy += r.randint(15, 30)
    self.money -= r.randint(10, 30)
    self.hunger -= r.randint(5, 10)


def work(self):
    print(" Час для роботи")
    self.money += r.randint(30, 70)
    self.happy -= r.randint(5, 15)
    self.health -= r.randint(5, 10)
    self.hunger -= r.randint(10, 15)

def eat(self):
    if self.money >= 20:
        print(" Час поїсти")
        self.money -= r.randint(15, 25)
        self.hunger += r.randint(30, 50)
        self.health += r.randint(5, 10)
    else:
        print(" Грошей на їжу немає! Треба працювати.")
        self.work()


def isAlive(self):
    if self.progress < 3:
        print(" Відрахування через погану успішність!")
        self.alive = False
    elif self.happy <= 10:
        print(" Депресія Студент кидає навчання.")
        self.alive = False
    elif self.money < 0:
        print(" Не яких тобі грошей, йди процювати.")
        self.work()
    elif self.hunger <= 0:
        print(" Він помер...")
        self.alive = False
    elif self.health <= 20:
        print(" Він захворів(!")
        self.alive = False


def everyday(self):
    print(
{self.happy}  {self.progress}  {self.money}  {self.health}  {self.hunger}")


def studyLife(self, day):
    print(f"\n День {day}")
    if self.hunger < 30:
        self.eat()
    elif self.health < 50:
        self.sleep()
    elif self.progress < 5:
        self.study()
    elif self.happy < 30:
        self.chill()
    elif self.money < 20:
        self.work()
    else:
        action = r.choice(["study", "chill", "sleep", "work"])
        getattr(self, action)()
    self.everyday()
    self.isAlive()


# === Запуск симуляції ===
st1 = Student('Олег')
print(f" Починається рік студента {st1.name}!")

for day in range(1, 366):  # Цілий рік (365 днів)
    if not st1.alive:
        break
    st1.studyLife(day)