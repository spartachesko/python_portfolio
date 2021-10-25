import simple_draw as sd


# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.


# СНЕГ

def snowfall_main():
    n = 20
    # Переменная length_of_snowflake не используется.
    # length_of_snowflake = sd.random_number(10, 100)
    snowflakes = []
    #  Переменная snowflake не используется.
    # snowflake = []

    # генерация списка из 20 снежинок
    for quantity_snowflakes in range(n):
        x = sd.random_number(50, 100)
        y = sd.random_number(720, 800)
        length_of_snowflake = sd.random_number(10, 25)
        snowflake = [x, y, length_of_snowflake]
        snowflakes.append(snowflake)

    while True:
        sd.start_drawing()

        for i, (x, y, length) in enumerate(snowflakes):

            if y < 0:
                # Если высота падения снежинки становится меньше нуля,то:
                point = sd.get_point(x, y)
                sd.snowflake(center=point, length=length, color=sd.background_color)
                x = sd.random_number(50, 100)  # генерация новой координаты х для новой снежинки
                y = sd.random_number(720, 800)  # генерация новой координаты у для новой снежинки
                length_of_snowflake = sd.random_number(10, 25)  # генерация новой длины для новой снежинки
                snowflake = [x, y, length_of_snowflake]  # генерация новой снежинки, взамен удаленной
                snowflakes[i] = snowflake  # замена снежинки по индексу
                break
            point = sd.get_point(x, y)

            sd.snowflake(center=point, length=length, color=sd.background_color)

            x += sd.random_number(-10, 10)
            y -= sd.random_number(1, 5)

            snowflakes[i] = [x, y, length]
            point2 = sd.get_point(x, y)
            sd.snowflake(center=point2, length=length, color=sd.COLOR_WHITE)

        sd.finish_drawing()

        sd.sleep(0.05)

        if sd.user_want_exit():
            break

# snowfall_main()
# sd.pause()
