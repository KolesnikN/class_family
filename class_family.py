from termcolor import cprint


class House:
    money = 100
    trash = 0
    food = 50
    cat_eat = 30

    def __init__(self, hom):
        self.hom = hom

    def __str__(self):
        res = super().__str__()
        return 'Дом на {} , в тумбочке денег {} , в холодильнике еды {} , мусора в доме {} '.format(
            self.hom, self.money, self.food, self.trash)


class Husband(House):
    hungry = 50
    happy = 100
    def __init__(self, hom, name):
        super().__init__(hom=hom)
        self.hom = hom
        self.name = name

    def __str__(self):
        super().__str__()
        return '{} сытость {} и счастье {}'.format(self.name, self.hungry, self.happy)

    def act(self):
        if self.hungry < 30:
            self.eat()
        elif self.happy < 30:
            self.gaming()
        elif House.money < 450:
            self.work()
        else:
            print('{} ничего не делает'.format(self.name))
            self.hungry -= 5
            House.trash += 5

    def eat(self):
        print('{} идёт кушать'.format(self.name))
        House.food -= 20
        House.trash += 5
        self.hungry += 30
        self.happy -= 5

    def work(self):
        print('{} идёт работать'.format(self.name))
        House.money += 200
        self.hungry -= 10
        self.happy -= 20

    def gaming(self):
        print('{} играет весь день'.format(self.name))
        self.hungry -= 10
        self.happy += 20
        House.trash += 5


class Wife(House):
    hungry = 50
    happy = 100
    def __init__(self, hom, name):
        super().__init__(hom=hom)
        self.hom = hom
        self.name = name

    def __str__(self):
        super().__str__()
        return '{} сытость {} и счастье {}'.format(self.name, self.hungry, self.happy)

    def act(self):
        if self.hungry < 30:
            self.eat()
        elif House.food < 30:
            self.shopping()
        elif self.happy < 30:
            self.buy_fur_coat()
        elif House.trash > 60:
            self.clean_house()
        else:
            print('{} ничего не делает'.format(self.name))
            self.hungry -= 10
            self.hungry -= 10
            House.trash += 5

    def eat(self):
        print('{} идёт кушать'.format(self.name))
        self.hungry += 30
        House.food -= 30
        House.trash += 5
        self.happy -= 5

    def shopping(self):
        print('{} идёт тратить деньги'.format(self.name))
        House.money -= 100
        House.food += 100
        House.trash += 5
        self.hungry -=10
        self.happy -= 10

    def buy_fur_coat(self):
        print('{} с Ником идут покупать шубу'.format(self.name))
        self.happy += 70
        self.hungry -= 10
        House.trash += 5

    def clean_house(self):
        print('{} идёт убираться'.format(self.name))
        House.trash -= 90
        self.happy -= 10

class Cat(House):
    hungry = 50
    happy = 100
    def __init__(self, hom, name):
        super().__init__(hom=hom)
        self.hom = hom
        self.name = name

    def __str__(self):
        super().__str__()
        return '{} сытость {} и счастье {}'.format(self.name, self.hungry, self.happy)

    def act(self):
        if self.hungry < 30:
            self.eat()
        elif self.happy < 20:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        print('{} идёт кушать'.format(self.name))
        self.hungry += 30
        House.food -= 30
        House.trash += 5
        self.happy -= 10

    def sleep(self):
        print('{} наелся и спит'.format(self.name))
        self.hungry -= 20
        House.trash += 5
        self.happy -= 10

    def soil(self):
        print('{} дерёт обои весь день'.format(self.name))
        self.hungry -= 30
        House.trash += 15
        self.happy += 30

class Child(House):
    hungry = 50
    happy = 100
    def __init__(self, hom, name):
        super().__init__(hom=hom)
        self.hom = hom
        self.name = name

    def __str__(self):
        super().__str__()
        return '{} сытость {} и счастье {}'.format(self.name, self.hungry, self.happy)

    def act(self):
        if self.hungry < 30:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        print('{} идёт кушать'.format(self.name))
        self.hungry += 30
        House.food -= 50
        House.trash += 5

    def sleep(self):
        print('{} наелся и спит'.format(self.name))
        self.hungry -= 20
        House.trash += 5

home = House(hom='Любимова')
nick = Husband(hom='Любимова', name='муж')
ulia = Wife(hom='Любимова', name='жена')
lorderon = Cat(hom='Любимова', name='котик')
child = Child(hom='Любимова', name='ребёнок')

for day in range(365):
    cprint('\nДень {0:*^36}'.format(day), color='white')
    nick.act()
    ulia.act()
    child.act()
    lorderon.act()
    cprint(nick, color='red')
    cprint(ulia, color='yellow')
    cprint(child, color='magenta')
    cprint(lorderon, color='cyan')
    cprint(home, color='blue')
