# -*- coding: utf-8 -*-
import os


# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

#  здесь ваш код

def doc_reader(file_name):
    with open(file_name, 'r') as txt:
        nok_count = 1
        lines = (line[1:17] for line in txt if line.endswith('NOK\n'))
        last_nok_time = next(lines)
        for line in lines:
            if last_nok_time == line:
                nok_count += 1
            else:
                yield last_nok_time, nok_count
                nok_count = 1
                last_nok_time = line
        yield last_nok_time, nok_count


path = 'events.txt'
path_normalized = os.path.normpath(path)
document = doc_reader(file_name=path_normalized)

for group_time, event_count in document:
    print(f'[{group_time}] {event_count}')
