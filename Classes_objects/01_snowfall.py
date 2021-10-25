# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    x = sd.random_number(50, 1000)
    y = sd.random_number(720, 800)
    length_of_snowflake = sd.random_number(10, 25)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length_of_snowflake, color=sd.background_color)

    def move(self):
        self.x += sd.random_number(-30, 30)
        self.y -= sd.random_number(1, 25)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length_of_snowflake, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y > 0


def get_flakes(count):
    snowflakes = []
    for count in range(count):
        snowflakes.append(Snowflake())
    return snowflakes


def get_fallen_flakes():
    count_snowflakes = 0
    for snowflake in flakes:
        if not snowflake.can_fall():
            count_snowflakes += 1
            index = flakes.index(snowflake)
            del flakes[index]
    return count_snowflakes


def append_flakes(count):
    for count in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=5)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes(count=fallen_flakes)

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
