# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowflakes, draw_snowflakes, move_snowflakes, numbers_of_snowflakes_bottom, \
    remove_snowflakes

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

print('Сколько снежинок хотите создать?')
n = int(input())
create_snowflakes(n)
while True:

    sd.start_drawing()

    draw_snowflakes(sd.background_color)

    move_snowflakes()

    draw_snowflakes(sd.COLOR_WHITE)
    sd.finish_drawing()

    list_for_removing = numbers_of_snowflakes_bottom()

    if len(list_for_removing) > 0:
        remove_snowflakes(list_for_removing)

        create_snowflakes(len(list_for_removing))

    sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()
