# -*- coding: utf-8 -*-

import os
import copy
import threading
import operator


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!

#  тут ваш код в многопоточном стиле


class TickReader(threading.Thread):

    def __init__(self, file_for_checking, *args, **kwargs):
        super(TickReader, self).__init__(*args, **kwargs)
        self.file_for_checking = file_for_checking
        self.secid = None
        self.volatility_percent = 0

    def run(self):
        with open(self.file_for_checking, "r") as txt:
            txt.readline()
            line_with_data = txt.readline()
            line_with_data = line_with_data.split(',')
            min_price = line_with_data[2]
            max_price = line_with_data[2]
            secid = line_with_data[0]

            for line in txt:
                line = line.rstrip()
                line = line.split(',')
                temp_price = line[2]

                if temp_price < min_price:
                    min_price = temp_price
                if temp_price > max_price:
                    max_price = temp_price
            half_sum = (float(max_price) + float(min_price)) / 2
            volatility_percent = ((float(max_price) - float(min_price)) / half_sum) * 100
            if volatility_percent < 0: volatility_percent = volatility_percent * (-1)
            self.volatility_percent = round(volatility_percent, 2)
            self.secid = secid


def files(path):
    for document in os.listdir(path):
        if document.endswith(".csv"):
            file_for_checking = os.path.join(path, document)
            yield file_for_checking


one_tickers_data = []
zero_list = []
list_volatility = []
directory = "trades"
path_normalized = os.path.normpath(directory)

tickers = [TickReader(file_for_checking=file) for file in files(path_normalized)]

for ticker in tickers:
    ticker.start()
    one_tickers_data = [ticker.secid, ticker.volatility_percent]
    if ticker.volatility_percent == 0:
        zero_list.append(ticker.secid)
    else:
        list_volatility.append(one_tickers_data)

for ticker in tickers:
    ticker.join()

print(f'Максимальная волатильность:')
list_max_tickers = sorted(list_volatility, key=operator.itemgetter(1), reverse=True)
count_max_ticker = 4
current_count_ticker = 0
for name, value in list_max_tickers:
    current_count_ticker += 1
    if current_count_ticker == count_max_ticker:
        break
    print(f'{name} - {value}')

print(f'Минимальная волатильность:')
list_max_tickers_reversed = sorted(list_volatility, key=operator.itemgetter(1), reverse=False)
list_min_tickers = copy.copy(list_max_tickers_reversed[0:3])
for name, value in sorted(list_min_tickers, key=operator.itemgetter(1), reverse=True):
    print(f'{name} - {value}')

print(f'Нулевая волатильность:')
zero_volatility = sorted(zero_list, reverse=False)
list_zero_tickers = copy.copy(zero_volatility)
print(list_zero_tickers)
