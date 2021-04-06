# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


# ####################################################### Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.mud = 0
        self.cat_food = 30

    def __str__(self):
        return 'Кол-во денег в тумбочке - {},кол-во еды в холодильнике - {},кол-во грязи - {}, ' \
               'кол-во кошачьей еды - {}'.format(self.money, self.food, self.mud, self.cat_food)


class Cat:
    house = None

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        return 'У - {} : Степень сытости - {}'.format(self.name, self.fullness)

    def settle(self, house):
        self.house = house
        return self

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер с голоду...'.format(self.name), color='red')
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.eat()
        else:
            self.soil()

    def eat(self):
        if self.house.cat_food >= 30:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} не нашел еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='yellow')
        self.fullness -= 10

    def soil(self):
        cprint('{} драл обои'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.mud += 5


class Human:
    house = None

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return 'У - {} : Степень сытости - {}, Степень счастья - {}'.format(self.name, self.fullness, self.happiness)

    def settle(self, house):
        self.house = house
        return self

    def act(self):
        if home.mud > 90:
            self.happiness -= 10

        if self.fullness <= 0:
            cprint('{} умер с голоду...'.format(self.name), color='red')
            return False

        if self.happiness <= 10:
            cprint('{} умер от скуки...'.format(self.name), color='red')
            return False
        return True

    def eat(self, portion_of_food):

        if self.house.food >= 30:

            self.fullness += portion_of_food
            self.house.food -= portion_of_food
            return True
        else:
            return False

    def pet_the_cat(self):
        self.happiness += 5
        self.fullness -= 10


class Child(Human):

    def act(self):

        if not super().act():
            return

        dice = randint(1, 2)
        portion_of_food = 10
        if self.fullness <= 30:

            self.eat(portion_of_food=portion_of_food)

        elif dice == 1:
            self.eat(portion_of_food=portion_of_food)
        else:
            self.sleep()
        self.happiness = 100

    def eat(self, portion_of_food):
        portion_of_food = 10
        if super().eat(portion_of_food=portion_of_food) is True:

            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} не нашел еды'.format(self.name), color='red')

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='yellow')
        self.fullness -= 10


class Husband(Human):

    def act(self):

        if not super().act():
            return

        dice = randint(1, 3)
        portion_of_food = 30
        if self.fullness <= 10:
            self.eat(portion_of_food=portion_of_food)

        elif dice == 1:
            self.work()
        elif dice == 2:
            self.gaming()
        else:
            self.eat(portion_of_food=portion_of_food)

    def eat(self, portion_of_food):
        portion_of_food = 30
        if super().eat(portion_of_food=portion_of_food) is True:

            cprint('{} поел'.format(self.name), color='yellow')
        else:
            cprint('{} не нашел еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def gaming(self):
        cprint('{} играл в WoT'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class Wife(Human):

    def act(self):
        if not super().act():
            return
        if self.house.mud >= 100:
            self.clean_house()
            return

        dice = randint(1, 4)
        portion_of_food = 30
        if self.fullness <= 10:
            self.eat(portion_of_food=portion_of_food)
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.shopping_cat_food()
        elif dice == 3:
            self.eat(portion_of_food=portion_of_food)

        else:
            if self.buy_fur_coat() is True:
                cprint('{} купила себе шубу'.format(self.name), color='magenta')
            else:
                self.act()

    def eat(self, portion_of_food):
        portion_of_food = 30
        if super().eat(portion_of_food=portion_of_food) is True:

            cprint('{} поела'.format(self.name), color='yellow')
        else:
            cprint('{} не нашла еды'.format(self.name), color='red')

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходила в магазин за едой коту'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        if self.house.money >= 360:

            self.house.money -= 350
            self.happiness += 60
            self.fullness -= 10
            return True
        else:
            return False

    def clean_house(self):

        self.fullness -= 10
        self.house.mud -= 100
        return cprint('{}  выдраила дом'.format(self.name), color='grey', on_color='on_white')


home = House()
serge = Husband(name='Сережа').settle(house=home)
masha = Wife(name='Маша').settle(house=home)
murzik = Cat(name='Мурзик').settle(house=home)
kolya = Child(name='Коля').settle(house=home)

for day in range(1, 365):
    cprint('================== День {} =================='.format(day), color='white')
    serge.act()
    masha.act()
    murzik.act()
    kolya.act()
    home.mud += 5
    cprint(home, color='cyan')
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(kolya, color='cyan')
