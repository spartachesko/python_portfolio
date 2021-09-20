# -*- coding: utf-8 -*-
import os
import copy
import operator
from multiprocessing import Process, Queue


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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

class TickReader(Process):

    def __init__(self, file_for_checking, ticker_info_receiver, *args, **kwargs):
        super(TickReader, self).__init__(*args, **kwargs)
        self.file_for_checking = file_for_checking
        self.secid = None
        self.volatility_percent = 0
        self.ticker_info_receiver = ticker_info_receiver

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
            if volatility_percent < 0:
                volatility_percent = volatility_percent * (-1)
            volatility_percent = round(volatility_percent, 2)
            self.ticker_info_receiver.put([secid, volatility_percent])


#

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
ticker_info = Queue()
tickers = [TickReader(file_for_checking=file, ticker_info_receiver=ticker_info) for file in files(path_normalized)]

for ticker in tickers:
    ticker.start()
for ticker in tickers:
    ticker.join()

for ticker in tickers:

    secid, volatility = ticker_info.get()
    one_tickers_data = [secid, volatility]
    if volatility == 0:
        zero_list.append(secid)
    else:
        list_volatility.append(one_tickers_data)

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

