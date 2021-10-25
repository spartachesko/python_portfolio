# -*- coding: utf-8 -*-
import simple_draw as sd
from events_for_drawings import house
from events_for_drawings import rainbow
from events_for_drawings import smile

from events_for_drawings import tree
from events_for_drawings import sun
from events_for_drawings import snowfall

sd.resolution = (1000, 700)

house.building()
rainbow.rainbow()
smile.smile()
tree.draw_branches_random()
sun.sun()
snowfall.snowfall_main()

# Создать пакет, в который скопировать функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)


sd.pause()

