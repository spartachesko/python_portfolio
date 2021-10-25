# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока Classes_objects/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
# +  подобрать кота - у кота появляется дом.
# +  купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
# +  убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# + Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# + Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.+
# + Когда кот спит - сытость уменьшается на 10+
# + Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.+
# + Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5+
# + Если степень сытости < 0, кот умирает.+
# + Так же надо реализовать метод "действуй" для кота, в котором он принимает решение+
# + что будет делать сегодня+

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
from termcolor import cprint


class Cat:
    def __init__(self, cat_name):
        self.fullness = 50
        self.house = None
        self.cat_name = cat_name

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.cat_name, self.fullness,
        )

    # def go_to_the_house(self, house):
    #     self.house = house
    #     cprint('{} Въехал в дом'.format(self.cat_name), color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('{} поел'.format(self.cat_name), color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10

    def sleep(self):
        cprint('{} поспал'.format(self.cat_name), color='yellow')
        self.fullness -= 10

    def crash_the_house(self):
        cprint('{} драл обои'.format(self.cat_name), color='yellow')
        self.fullness -= 10
        self.house.mud += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.cat_name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
            #  почему дохнет кот? условие ведь прописано, чтобы он ел, когда становится голодным
            #  Проверьте в режиме отладки правильность работы этого метода.
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.crash_the_house()
        else:
            self.eat()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        # self.cat_name =

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness,
        )

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_cat_food(self):
        cprint('{} сходил в магазин за едой коту'.format(self.name), color='magenta')
        self.house.money -= 50
        self.house.cat_food += 50

    def cleaning_house(self):
        cprint('{} убрал дом'.format(self.name), color='white')
        self.house.mud -= 100
        self.fullness -= 20

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='cyan')

    def take_cat(self, cat_in_house):
        #  Аргумент house не используется и его можно убрать.

        #  Аргумент с именем cat существует не только внутри
        #  функции, но и на уровне видимости модуля. Иногда подобное
        #  совпадение имеён может привести к труднодиагностируемым ошибкам.
        #  Нужно переименовать переменную либо в функции либо в цикле.

        cat_in_house.house = self.house
        cprint('{} Приютили в дом'.format(self.house.cat_name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.cat_food < 10:
            self.shopping_cat_food()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 50
        self.mud = 0
        self.cat_name = 'Борис Бритва'

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {},еды для кота осталось {}'.format(
            self.food, self.money, self.cat_food
        )


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
    # Cat(cat_name='Борис Бритва')
]
pets = [Cat(cat_name='Борис Бритва')]

my_sweet_home = House()
# cat_name()

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

# for cat in pets:
#     cat.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))

    if day == 3:
        for cat in pets:
            citizens[randint(0, len(citizens))].take_cat(cat_in_house=cat)

    else:
        for citisen in citizens:
            citisen.act()
    if day > 3:
        for cat in pets:
            cat.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    if day > 3:
        for cat in pets:
            print(cat)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

# Зачёт!
