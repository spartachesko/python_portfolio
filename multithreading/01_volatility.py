# -*- coding: utf-8 -*-
import collections
import os
import copy


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/multithreading/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>

#  написать код в однопоточном/однопроцессорном стиле

class TickReader:

    def __init__(self, file_for_checking):
        self.file_for_checking = file_for_checking

    def run(self, file_for_checking):
        with open(file_for_checking, "r") as txt:
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
        return secid, round(volatility_percent, 2)


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

for file in files(path_normalized):
    ticker = TickReader(file_for_checking=file)
    name, volatility = ticker.run(file_for_checking=file)
    one_tickers_data = [name, volatility]
    if volatility == 0:
        zero_list.append(name)
    else:
        list_volatility.append(one_tickers_data)

print(f'Максимальная волатильность:')
list_max_tickers = sorted(list_volatility, key=lambda k: k[1], reverse=True)
count_max_ticker = 4
current_count_ticker = 0
for name, value in list_max_tickers:
    current_count_ticker += 1
    if current_count_ticker == count_max_ticker:
        break
    print(f'{name} - {value}')

print(f'Минимальная волатильность:')
list_max_tickers_reversed = sorted(list_volatility, key=lambda k: k[1], reverse=False)
list_min_tickers = copy.copy(list_max_tickers_reversed[0:3])
for name, value in sorted(list_min_tickers, key=lambda k: k[1], reverse=True):
    print(f'{name} - {value}')

print(f'Нулевая волатильность:')
zero_volatility = sorted(zero_list, reverse=False)
list_zero_tickers = copy.copy(zero_volatility)
print(list_zero_tickers)

