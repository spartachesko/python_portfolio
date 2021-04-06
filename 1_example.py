#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

table_code = goods['Стол']
table_item_1 = store[table_code][0]
table_item_2 = store[table_code][1]
table_quantity_1 = table_item_1['quantity']
table_quantity_2 = table_item_2['quantity']
table_quantity = table_quantity_1 + table_quantity_2
table_price_1 = table_item_1['price']
table_price_2 = table_item_2['price']
table_cost_1 = table_quantity_1*table_price_1
table_cost_2 = table_quantity_2*table_price_2
table_cost = table_cost_1 + table_cost_2
print('Стол  -', table_quantity, 'шт, стоимость', table_cost, 'руб')


sofa_code = goods['Диван']
sofa_item_1 = store[sofa_code][0]
sofa_item_2 = store[sofa_code][1]
sofa_quantity_1 = sofa_item_1['quantity']
sofa_quantity_2 = sofa_item_2['quantity']
sofa_quantity = sofa_quantity_1 + sofa_quantity_2
sofa_price_1 = sofa_item_1['price']
sofa_price_2 = sofa_item_2['price']
sofa_cost_1 = sofa_quantity_1*sofa_price_1
sofa_cost_2 = sofa_quantity_2*sofa_price_2
sofa_cost = sofa_cost_1 + sofa_cost_2
print('Диван  -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')


chair_code = goods['Стул']
chair_item_1 = store[chair_code][0]
chair_item_2 = store[chair_code][1]
chair_item_3 = store[chair_code][2]
chair_quantity_1 = chair_item_1['quantity']
chair_quantity_2 = chair_item_2['quantity']
chair_quantity_3 = chair_item_3['quantity']
chair_quantity = chair_quantity_1 + chair_quantity_2 + chair_quantity_3
chair_price_1 = chair_item_1['price']
chair_price_2 = chair_item_2['price']
chair_price_3 = chair_item_3['price']
chair_cost_1 = chair_quantity_1*chair_price_1
chair_cost_2 = chair_quantity_2*chair_price_2
chair_cost_3 = chair_quantity_3*chair_price_3
chair_cost = chair_cost_1 + chair_cost_2 + chair_cost_3
print('Стул  -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')


