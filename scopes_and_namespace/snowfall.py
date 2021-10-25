import simple_draw as sd

snowflakes = []


def create_snowflakes(n):
    for quantity_snowflakes in range(n):
        x = sd.random_number(50, 1000)
        y = sd.random_number(720, 800)
        length_of_snowflake = sd.random_number(10, 25)
        snowflake = [x, y, length_of_snowflake]
        snowflakes.append(snowflake)


def draw_snowflakes(color):
    for snowflake in snowflakes:
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=snowflake[2], color=color)


def move_snowflakes():
    for snowflake in snowflakes:
        snowflake[0] += sd.random_number(-30, 30)
        snowflake[1] -= sd.random_number(1, 25)


def numbers_of_snowflakes_bottom():
    list_for_removing = []

    for index_snowflake in range(len(snowflakes)):
        if snowflakes[index_snowflake][1] < 0:
            list_for_removing.append(index_snowflake)

    return list_for_removing


def remove_snowflakes(list_for_removing):
    list_for_removing = reversed(list_for_removing)
    for index_snowflake in list_for_removing:
        del snowflakes[index_snowflake]
