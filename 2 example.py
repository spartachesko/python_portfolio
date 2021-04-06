import simple_draw as sd

sd.resolution = (1000, 700)

N = 20

length_of_snowflake = sd.random_number(10, 100)
snowflakes = []
snowflake = []


for quantity_snowflakes in range(N):
    x = sd.random_number(50, 1000)
    y = sd.random_number(720, 800)
    length_of_snowflake = sd.random_number(10, 25)
    snowflake = [x, y, length_of_snowflake]
    snowflakes.append(snowflake)

while True:

    sd.start_drawing()

    for i, (x, y, length) in enumerate(snowflakes):

        if y < 0:

            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=length, color=sd.background_color)

            x = sd.random_number(50, 1000)
            y = sd.random_number(720, 800)
            length_of_snowflake = sd.random_number(10, 25)
            snowflake = [x, y, length_of_snowflake]

            snowflakes[i] = snowflake
        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=sd.background_color)

        x += sd.random_number(-30, 30)
        y -= sd.random_number(1, 25)
        snowflakes[i] = [x, y, length]
        point2 = sd.get_point(x, y)
        sd.snowflake(center=point2, length=length, color=sd.COLOR_WHITE)

    sd.finish_drawing()

    sd.sleep(0.05)

    if sd.user_want_exit():
        break
sd.pause()