# -*- coding: utf-8 -*-
import re


# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

#  здесь ваш код
#
class ValueError(Exception):
    pass


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def checking(line):
    reg_data = line.split(' ')
    if len(reg_data) == 3:
        if not reg_data[0].isalpha():
            raise NotNameError('Ошибка в имени')

        if not reg_data[1].find('@') != -1 and not reg_data[1].find('.') != -1:
            raise NotEmailError('Ошибка в почте')

        if reg_data[2].isdigit():
            age = int(reg_data[2])
            if not 100 > age > 9:
                raise ValueError('Ошибка в возрасте')

    else:
        raise ValueError('Недостаточно данных')


with open('registrations.txt', mode='r') as ff:
    good_file = open('registrations_good.log', mode='w')
    bad_file = open('registrations_bad.log', mode='w')
    for line in ff:
        line = line[:-1]
        try:
            checking(line)
            good_file.write(line)
            good_file.write('\n')
        except (ValueError, NotEmailError, NotNameError) as exc:
            bad_file.write(line + ' Ошибка: ' + type(exc).__name__)
            bad_file.write('\n')
    good_file.close()
    bad_file.close()
