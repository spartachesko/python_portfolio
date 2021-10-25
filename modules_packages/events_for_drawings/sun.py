import simple_draw as sd


# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)

def sun():
    x_center = 700
    y_center = 500
    center_position = sd.get_point(x_center, y_center)  # центр для отрисовки круга
    sd.circle(center_position, radius=40, color=sd.COLOR_YELLOW, width=0)  # создание центра круга
    for angle in range(0, 361, 45):  # создание лучей
        v1 = sd.get_vector(start_point=center_position, angle=angle, length=100, width=6)
        v1.draw(color=sd.COLOR_YELLOW)

#
# sun()
