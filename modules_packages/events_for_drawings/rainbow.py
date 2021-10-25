import simple_draw as sd

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.


# РАДУГА


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow():
    start_point_x = 300
    start_point_y = 0
    radius = 790
    step = 20
    for color in rainbow_colors:
        center_position = sd.get_point(start_point_x, start_point_y)
        sd.circle(center_position, radius, color, width=step - 1)
        radius += step

# rainbow()
