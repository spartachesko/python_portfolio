# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 900)
root_point = sd.get_point(300, 30)


def draw_branches_random(start_point, delta, length, angle):
    if length < 5:
        return

    v1 = sd.get_vector(start_point, angle=angle, length=length, width=2)
    v1.draw()
    next_point = v1.end_point
    variance_length = float(sd.random_number(6, 9) / 10)
    variance_angle = float(sd.random_number(12, 42))
    next_angle = angle - variance_angle
    next_length = length * variance_length
    draw_branches_random(start_point=next_point, angle=next_angle, length=next_length, delta=delta)
    next_angle = angle + variance_angle
    draw_branches_random(start_point=next_point, angle=next_angle, length=next_length, delta=delta)


draw_branches_random(start_point=root_point, delta=30, length=100, angle=90)

sd.pause()
