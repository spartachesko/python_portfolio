# -*- coding: utf-8 -*-
import zipfile
import os
import collections
import operator


# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

class DescendingFrequency:
    variable = 1
    variable_bool = True

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = collections.defaultdict(int)
        self.sorted_stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        filename = zfile.namelist()[0]
        zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as txt:
            for line in txt:
                self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                self.stat[char] += 1

    def print_result(self):
        total = 0
        print('+{txt:^10}+'.format(txt='------------------------'))
        print('|{txt_1:^10}  | {txt_2:^10}|'.format(txt_1='буква', txt_2='частота'))
        print('+{txt:^10}+'.format(txt='------------------------'))

        for i in self.sorted_keys():
            self.sorted_stat[i] = self.stat[i]

        for key in self.sorted_stat:
            print('|{txt:^10}  | {result:^10}|'.format(txt=key[0], result=key[1]))
            total += key[1]
        print('+{txt:^10}+'.format(txt='------------------------'))
        print('|{txt:^10}  | {result:^10}|'.format(txt='итого', result=total))
        print('+{txt:^10}+'.format(txt='------------------------'))

    def sorted_keys(self):
        sorted_keys = sorted(self.stat.items(), key=operator.itemgetter(self.variable), reverse=self.variable_bool)
        return sorted_keys


class AscendingFrequency(DescendingFrequency):
    variable = 1
    variable_bool = False


class DescendingAlphabet(DescendingFrequency):
    variable = 0
    variable_bool = False


class AscendingAlphabet(DescendingFrequency):
    variable = 0
    variable_bool = True


path = 'python_snippets/voyna-i-mir.txt.zip'
path_normalized = os.path.normpath(path)
descending_frequency = DescendingFrequency(file_name=path_normalized)
descending_frequency.collect()
descending_frequency.print_result()

#   - по частоте по возрастанию
ascending_frequency = AscendingFrequency(file_name=path_normalized)
ascending_frequency.collect()
ascending_frequency.print_result()
#  - по алфавиту по возрастанию
ascending_alphabet = AscendingAlphabet(file_name=path_normalized)
ascending_alphabet.collect()
ascending_alphabet.print_result()

#  - по алфавиту по убыванию

descending_alphabet = DescendingAlphabet(file_name=path_normalized)
descending_alphabet.collect()
descending_alphabet.print_result()

# Зачёт!
