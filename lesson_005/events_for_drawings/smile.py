import simple_draw as sd


# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.


# СМАЙЛ
# delta_x = 370
# delta_y = -40


def smile():
    delta_x = 370
    delta_y = -40

    x_in_def = 50
    y_in_def = 50
    color_in_def = sd.COLOR_WHITE

    left_start_point_x = 0 + x_in_def + delta_x
    left_start_point_y = 0 + y_in_def + delta_y
    right_start_point_x = 70 + x_in_def + delta_x
    right_start_point_y = 50 + y_in_def + delta_y
    center_position_left_eye = sd.get_point(left_start_point_x + 20 + x_in_def, left_start_point_y + 30 + y_in_def)
    center_position_right_eye = sd.get_point(left_start_point_x + 50 + x_in_def, left_start_point_y + 30 + y_in_def)
    left_bottom = sd.get_point(left_start_point_x + x_in_def, left_start_point_y + y_in_def)
    right_top = sd.get_point(right_start_point_x + x_in_def, right_start_point_y + y_in_def)
    point_1 = sd.get_point(left_start_point_x + x_in_def + 20, left_start_point_y + 20 + y_in_def)
    point_2 = sd.get_point(left_start_point_x + x_in_def + 25, left_start_point_y + 15 + y_in_def)
    point_3 = sd.get_point(left_start_point_x + x_in_def + 45, left_start_point_y + 15 + y_in_def)
    point_4 = sd.get_point(left_start_point_x + x_in_def + 50, left_start_point_y + 20 + y_in_def)
    point_list = (point_1, point_2, point_3, point_4)
    sd.ellipse(left_bottom=left_bottom, right_top=right_top, color=color_in_def, width=1)
    sd.circle(center_position=center_position_left_eye, radius=5, color=color_in_def, width=1)
    sd.circle(center_position=center_position_right_eye, radius=5, color=color_in_def, width=1)
    sd.lines(point_list=point_list, color=color_in_def, closed=False, width=1)

# x_in_def, y_in_def, color_in_def, delta_x, delta_y
# x = 50
# y = 50
# color = sd.COLOR_WHITE
# smile(x, y, color, delta_x, delta_y)
