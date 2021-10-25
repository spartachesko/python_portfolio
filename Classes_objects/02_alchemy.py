# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__

# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __str__(self):
        return 'вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        else:
            return None


class Air:

    def __str__(self):
        return 'воздух'

    def __add__(self, other):

        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return None


class Fire:

    def __str__(self):
        return 'огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:

    def __str__(self):
        return 'земля'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava()
        if isinstance(other, Water):
            return Mud()
        if isinstance(other, Air):
            return Dust()
        else:
            return None


class Lightning:

    def __str__(self):
        return 'молния'


class Mud:

    def __str__(self):
        return 'грязь'


class Storm:

    def __str__(self):
        return 'шторм'


class Lava:

    def __str__(self):
        return 'лава'


class Steam:

    def __str__(self):
        return 'пар'


class Dust:

    def __str__(self):
        return 'пыль'


#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#  Добавьте примеры взаимодействия элементов.
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
