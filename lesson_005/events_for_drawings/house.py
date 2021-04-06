# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# Строим дом
import simple_draw as sd


# sd.resolution = (800, 500)


#  все элементы дома нужно разбивать на функции или это необязательно?
#  Рисовать каждую часть дома отдельной функцией не нужно.
#  Достаточно, чтобы можно было рисовать дом вызовом
#  функции из основного модуля задания. Из основной функциии
#  можно вызывать функции рисования частей дома.
# delta = 300


def building():
    delta = 300
    # параметры кирпича
    height_brick = 12.5
    width_brick = 25
    color = sd.COLOR_DARK_ORANGE

    for y in range(12):  # цикл переборки строк для кирпичной кладки
        shift = y % 2 / 2  # Вычисление коэфициента для сдвига крипчиной кладки
        row_x = width_brick * shift  # привязка сдвига к ряду кирпичной кладки

        for x in range(10):  # цикл укладки кирпичей
            left_bottom_x = width_brick * x - row_x
            left_bottom_y = height_brick * y
            right_top_x = left_bottom_x + width_brick
            right_top_y = left_bottom_y + height_brick
            left_bottom = sd.get_point(left_bottom_x + 80 + delta, left_bottom_y)
            right_bottom = sd.get_point(right_top_x + 80 + delta, right_top_y)
            sd.rectangle(left_bottom, right_bottom, color, width=2)

    # создаем условия для стен дома
    height_walls_y_right_top = height_brick * 12
    width_walls_x_right_bottom = width_brick * 10 + 80
    left_bottom_walls = sd.get_point(67 + delta, 0)
    right_top_walls = sd.get_point(width_walls_x_right_bottom + delta, height_walls_y_right_top)
    # строим обводку стен
    sd.rectangle(left_bottom_walls, right_top_walls, color, width=2)

    # РИСУЕМ КРЫШУ

    #    Переменная с именем prime существует не только внутри
    #  функции, но и на уровне видимости модуля. Иногда подобное
    #  совпадение имеён может привести к труднодиагностируемым ошибкам.
    #  Нужно переименовать переменную либо в функции либо в цикле.
    def roof(point_list_roof):
        sd.polygon(point_list_roof, color=(255, 43, 43), width=0)

    point_0 = sd.get_point(50 + delta, height_walls_y_right_top)
    point_1 = sd.get_point(width_walls_x_right_bottom + 20 + delta, height_walls_y_right_top)
    point_2 = sd.get_point((width_walls_x_right_bottom + 70) / 2 + delta, height_walls_y_right_top + 85)
    point_list = [point_0, point_1, point_2]
    roof(point_list)

    # Рисуем окно
    point_3 = sd.get_point(150 + delta, height_walls_y_right_top / 2 - 25)
    point_4 = sd.get_point(width_walls_x_right_bottom - 85 + delta, height_walls_y_right_top / 2 - 25)
    point_5 = sd.get_point(width_walls_x_right_bottom - 85 + delta, height_walls_y_right_top / 2 + 50)
    point_6 = sd.get_point(150 + delta, height_walls_y_right_top / 2 + 50)

    point_list_window = [point_3, point_4, point_5, point_6]

    #  Переменная с именем prime существует не только внутри
    #  функции, но и на уровне видимости модуля. Иногда подобное
    #  совпадение имеён может привести к труднодиагностируемым ошибкам.
    #  Нужно переименовать переменную либо в функции либо в цикле.
    def window(point_list_def_window):
        sd.polygon(point_list_def_window, color=(24, 144, 255), width=0)

    window(point_list_def_window=point_list_window)

# building(delta)

# sd.pause()
