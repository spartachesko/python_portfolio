# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.
sd.resolution = (1300, 800)
COLOR = sd.COLOR_RED


def get_polygon(n):
    def calc_step(point, angle, length):
        first_step = 180 * (n - 2) / n
        step = int(180 - first_step)

        return draw_polygon(point, step, length, angle)

    def draw_polygon(point, step, length, angle):
        next_point = point
        for shape_angle in range(0, 300, step):
            v1 = sd.get_vector(start_point=next_point, angle=shape_angle + angle, length=length, width=1)
            v1.draw(color=COLOR)
            next_point = v1.end_point
        sd.line(start_point=next_point, end_point=point, color=COLOR, width=1)

    return calc_step


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
