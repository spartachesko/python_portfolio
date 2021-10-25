import simple_draw as sd

sd.resolution = (1000, 700)


# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.


# ДЕРЕВО

# root_point = sd.get_point(800, 0)
# start_point = sd.get_point(800, 0)
# length = 70
# angle = 90
# delta = 30


def draw_branches_random(start_point=sd.get_point(800, 0), angle=90.0, length=70.0, delta=30):
    # Изменил аргументы по умолчанию с целых чисел на числа с плавающей запятой.
    #  Так не будет замечаний среды разработки.
    # start_point = sd.get_point(800, 0)
    # length = 70
    # angle = 90
    # delta = 30
    if length < 5:
        return
    if length < 10:
        color = sd.COLOR_GREEN
    #  Замените второй if на else, чтобы убрать предупреждение
    #  о том, что переменная color может не существовать.
    else:
        color = (91, 58, 41)

    v1 = sd.get_vector(start_point, angle=angle, length=length, width=2)
    v1.draw(color)
    next_point = v1.end_point
    variance_length = float(sd.random_number(6, 9) / 10)
    variance_angle = float(sd.random_number(12, 42))
    next_angle = angle - variance_angle
    next_length = length * variance_length
    draw_branches_random(start_point=next_point, angle=next_angle, length=next_length, delta=delta)
    next_angle = angle + variance_angle
    draw_branches_random(start_point=next_point, angle=next_angle, length=next_length, delta=delta)

# draw_branches_random(start_point=root_point, delta=delta, length=length, angle=angle)

# sd.pause()
