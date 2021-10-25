# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."


# с помощью фукций из my_burger и вывести на консоль.


from my_burger import bun, cutlets, cucumbers, tomato, onion, mayonnaise, cheese, sauce, ketchup

import pprint

pprint.pprint('Всем привет, сегодня будем готовить тройной чизбургер и двойной чизбургер.')
bun()
cutlets()
cucumbers()
tomato()
onion()
mayonnaise()
cheese()
sauce()
ketchup()
bun()
print("Наш бургер готов!Приступим к приготовлению двойного чизбургера.")

bun()
cutlets()
cucumbers()
tomato()
mayonnaise()
cheese()

print('На сегодня все!')
