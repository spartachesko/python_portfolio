# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана
COLOR = sd.COLOR_RED


def triangle(point, length, delta):
    draw_polygon(point=point, step=120, length=length, delta=delta)


def square(point, delta, length):
    draw_polygon(point=point, step=90, length=length, delta=delta)


def pentagon(point, delta, length):
    draw_polygon(point=point, step=60, length=length, delta=delta)


def hexagon(point, delta, length):
    draw_polygon(point=point, step=72, length=length, delta=delta)


shapes = {'0': {'name': 'треугольник', 'shape': triangle}, '1': {'name': 'квадрат', 'shape': square},
          '2': {'name': 'пятиугольник', 'shape': pentagon}, '3': {'name': 'шестиугольник', 'shape': hexagon}, }


def draw_polygon(point, step, length, delta):
    next_point = point
    for angle in range(0, 300, step):
        v1 = sd.get_vector(start_point=next_point, angle=angle + delta, length=length, width=1)
        v1.draw(color=sd.COLOR_RED)
        next_point = v1.end_point
    sd.line(start_point=next_point, end_point=point, color=sd.COLOR_RED, width=1)


def draw(number_of_shape_draw):
    kind_of_shape = shapes[number_of_shape_draw]['shape']

    start_point = sd.get_point(250, 250)
    kind_of_shape(point=start_point, length=150, delta=20)


print('Возможные фигуры:')

for value in shapes:
    print(value, ':', shapes[value]['name'])

number_of_shape = input('Введите желаемую фигуру: ')
while number_of_shape not in shapes:
    print('Вы ввели некорректный номер!')
    number_of_shape = input('Введите желаемую фигуру: ')

draw(number_of_shape, color=COLOR)

sd.pause()
