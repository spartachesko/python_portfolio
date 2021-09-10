# -*- coding: utf-8 -*-
from random import randint

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возм0о0000жен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
carma = 0


class MainException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class IamGodError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DrunkError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class CarCrashError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class GluttonyError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DepressionError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class SuicideError(MainException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def one_day():
    level_of_carma = randint(1, 13)
    if level_of_carma >= 8:
        exception_class = list_of_exception[level_of_carma - 8]
        raise exception_class(exception_class.__name__)

    else:
        return level_of_carma


list_of_exception = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
while True:

    try:

        value_carma = one_day()
        carma += value_carma
    except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
        print(f'Что-то пошло не так: {exc}, но мы устояли')

    if carma >= ENLIGHTENMENT_CARMA_LEVEL:
        break
