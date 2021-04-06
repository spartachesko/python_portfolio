# -*- coding: utf-8 -*-
import os
import collections


# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# [2018-05-17 01:57] 1234
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

#  здесь ваш код
class Minute:
    position = 17

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = collections.defaultdict(int)

    def collect(self):

        with open(self.file_name, 'r') as txt:
            for line in txt:
                line = line.rstrip()
                if line.endswith('NOK'):
                    minute_in_line = line[0:self.position] + ']'
                    self.data[minute_in_line] += 1

    def print_result(self, file_parsed=None):
        file = open(file_parsed, 'w', encoding='utf8')
        for item in self.data:
            file.write(item + ' ' + str(self.data[item]) + '\n')
        file.close()


class Hour(Minute):
    position = 14


class Month(Minute):
    position = 8


class Year(Minute):
    position = 5


path = 'events.txt'
path_normalized = os.path.normpath(path)
document = Minute(file_name=path_normalized)
document.collect()
document.print_result(file_parsed='result_after_parcing_Minute.txt')
document = Hour(file_name=path_normalized)
document.collect()
document.print_result(file_parsed='result_after_parcing_Hour.txt')
document = Month(file_name=path_normalized)
document.collect()
document.print_result(file_parsed='result_after_parcing_Month.txt')
document = Year(file_name=path_normalized)
document.collect()
document.print_result(file_parsed='result_after_parcing_Year.txt')


