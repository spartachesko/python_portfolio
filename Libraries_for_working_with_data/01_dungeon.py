# -*- coding: utf-8 -*-
import json
import re
import time
from decimal import Decimal
import csv
import warnings

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...


remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']
# experience = 0

with open('rpg.json', 'r') as read_file:
    dungeon = json.load(read_file)

with open('dungeon.csv', 'a', newline='') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(field_names)


def game_over(dungeon):
    """Проверка конца игры"""

    if len(dungeon) == 0 and not winner_flag:
        print(f'Вы в тупике! Скажите буль-буль ;)')
        exit()

    if winner_flag:
        exit()

    if current_remaining_time <= 0:
        print(f'Время вышло...пора купаться ;D ')
        exit()

    if hatch_closed:
        print(f'\nЧтобы открыть люк и выбраться на свободу, вам требуется 280 очков опыта.\n'
              f'У вас {experience} очков.\n'
              f'Задержите дыхание, удачного плавания ;)')
        exit()


def monsters_locations_lists(value_dungeon):
    """Функция возвращающая список монстров и локаций"""

    counter_location = 0
    counter_monster = 0
    list_locations = []
    list_monsters = []
    for event in value_dungeon:
        # если перед нами монстр
        if type(event) == str:

            counter_monster += 1
            position_monster_list = counter_monster
            list_monster = []
            list_monster.append(position_monster_list)
            list_monster.append(event)
            list_monsters.append(list_monster)
        # если перед нами локация
        else:
            counter_location += 1
            position_location_list = counter_location
            element_list = list(event.keys())
            list_location = []
            list_location.append(position_location_list)
            list_location.append(element_list[0])
            list_locations.append(list_location)

    return list_monsters, list_locations


def parcing_location_time(chosen_location):
    """Парсинг локации и времени"""

    # если выигрышная локация
    if 'Hatch' in chosen_location:

        if experience >= 280:
            pattern = r'([a-zA-Z]+)\_[t][m](\d+\.\d+)'
            matched = re.search(pattern, chosen_location)
            pattern_location = matched[1]
            pattern_time = Decimal(matched[2])

        else:
            global hatch_closed
            hatch_closed = True
            exit()

    # если локация забирает не целое кол-во секунд
    elif '.' in chosen_location:

        pattern = r'([a-zA-Z]+)\_(.+)\_[t][m](\d+\.\d+)'
        matched = re.search(pattern, chosen_location)
        pattern_location = matched[2]
        pattern_time = Decimal(matched[3])

    # если целое кол-во секунд
    else:
        # pattern = r'([a-zA-Z]+).(\d+).[t][m](\d+)'
        pattern = r'([a-zA-Z]+)\_(.+)\_[t][m](\d+)'
        matched = re.search(pattern, chosen_location)
        pattern_location = matched[2]
        pattern_time = Decimal(matched[3])

    return pattern_location, pattern_time


def parcing_exp_time(chosen_monster):
    """Парсинг опыта и времени"""

    # pattern = r'(.+)[e][x][p](\d+)\_[t][m](\d+)'
    pattern = r'(?P<type>Mob|Boss|Boss[\d]+)_exp(?P<exp>\d+)_tm(?P<time>\d+)'
    matched = re.search(pattern, chosen_monster)

    pattern_exp = int(matched[2])
    pattern_time = Decimal(matched[3])
    return pattern_exp, pattern_time

# выбор осуществляется тут
def fight(dungeon, list_monsters):
    """Сражение с монстрами"""

    for number, monster in list_monsters:
        print(f'{number} - {monster}')

    chosen_monster = input(f'Выберите монстра: ')

    # проверяем, что введено число
    try:
        chosen_monster = int(chosen_monster)
    except:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        dungeon = fight(dungeon, list_monsters)
        return dungeon

    # проверка наличия такого элемента в списке монстров
    if chosen_monster not in range(1, len(list_monsters)+1):
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        dungeon = fight(dungeon, list_monsters)
        return dungeon

    chosen_monster = chosen_monster - 1

    for element in dungeon:
        if type(element) == str:
            try:
                if element == dungeon[chosen_monster]:
                    dungeon.remove(element)
                    experience_monster, time_monster = parcing_exp_time(chosen_monster=element)

                    # подсчет оставшегося времени
                    global current_remaining_time
                    current_remaining_time -= time_monster

                    # подсчет опыта
                    global experience
                    experience += experience_monster

                    elapsed = time.monotonic() - start
                    elapsed = (f'{elapsed: 1.0f}')
                    global current_date
                    current_date = elapsed

                    print(f'\nУ вас {experience} опыта и осталось {current_remaining_time} секунд до наводнения\n'
                          f'Времени прошло {elapsed} сек\n')



            except:
                continue

    return dungeon

# выбор осуществляется тут
def monsters(dungeon, list_monsters):
    """Действия при наличии только монстров"""

    for number, monster in list_monsters:
        print(f' - Монстра - {number} - {monster}')

    print(f'Выберите действие:\n'
          f'1.Атаковать монстра\n'
          f'2.Сдаться и выйти из игры\n')

    chosen_action = input(f'Ваш выбор: ')

    # проверяем, что введено число
    try:
        chosen_action = int(chosen_action)
    except:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        monsters(dungeon, list_monsters)


    if int(chosen_action) == 1:
        # если решил сразиться с монстрами
        print(f'\n Вы выбрали сражаться с монстрами!\n')
        dungeon = fight(dungeon=dungeon, list_monsters=list_monsters)

        main_game(dungeon=dungeon)

    # сдаться и выйти из игры
    elif int(chosen_action) == 2:
        print(f'Не хватило духу доиграть..Эх,ты!')
        exit()

    else:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        monsters(dungeon, list_monsters)

# выбор осуществляется тут
def change_location(dungeon, list_locations):
    """  Смена локации """

    for number, location in list_locations:
        print(f'{number} - {location}')
    chosen_location = input(f'Выберите локацию: ')

    # проверяем, что введено число
    try:
        chosen_location = int(chosen_location)
    except:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        dungeon = change_location(dungeon,list_locations)
        return dungeon

    # проверка наличия такого элемента в списке локаций
    if chosen_location not in range(1, len(list_locations)+1):
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        dungeon = change_location(dungeon, list_locations)
        return dungeon

    chosen_location = list_locations[chosen_location - 1][1]


    # поиск словаря ,для вычленения нужной локации
    for element in dungeon:
        if type(element) == dict:
            try:
                dungeon = element[chosen_location]

                # получение номера локации и времени на прохождение
                number_location, time_location = parcing_location_time(chosen_location=chosen_location)

                # подсчет оставшегося времени
                global current_remaining_time
                current_remaining_time -= time_location

                # если открыт люк
                if number_location == 'Hatch':
                    print(dungeon)
                    global winner_flag
                    winner_flag = True
                    exit()

                elapsed = time.monotonic() - start
                elapsed = (f'{elapsed: 1.0f}')
                global current_date
                current_date = elapsed

                print(f'\nВы находитесь в локации - {chosen_location}\n'
                      f'У вас {experience} опыта и осталось {current_remaining_time} секунд до наводнения\n'
                      f'Времени прошло {elapsed} сек')

                # логирование в csv локации
                one_more_location = {'current_location': number_location, 'current_experience': experience,
                                     'current_date': current_date}
                with open('dungeon.csv', 'a', newline='') as out_csv:
                    writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
                    writer.writerow(one_more_location)

            except:

                continue

    return dungeon

# выбор осуществляется тут
def monsters_with_locations(dungeon, list_monsters, list_locations):
    """Действия при наличии монстров и локаций"""

    for number, monster in list_monsters:
        print(f' - Монстра - {number} - {monster}')

    for number, location in list_locations:
        print(f' - Вход в локацию: - {number} - {location}')

    print(f'Выберите действие:\n'
          f'1.Атаковать монстра\n'
          f'2.Перейти в другую локацию\n'
          f'3.Сдаться и выйти из игры\n')

    chosen_action = input(f'Ваш выбор: ')

    # проверяем, что введено число
    try:
        chosen_action = int(chosen_action)
    except:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        monsters_with_locations(dungeon, list_monsters, list_locations)


    # если есть монстры, но решил сменить локацию
    if int(chosen_action) == 2:
        dungeon = change_location(dungeon=dungeon, list_locations=list_locations)

        main_game(dungeon=dungeon)

    # если есть монстры, и решил сразиться с ними
    elif int(chosen_action) == 1:
        dungeon = fight(dungeon=dungeon, list_monsters=list_monsters)
        main_game(dungeon=dungeon)

    # сдаться и выйти из игры
    elif int(chosen_action) == 3:
        print(f'Не хватило духу доиграть..Эх,ты!')
        exit()


# выбор осуществляется тут
def locations(dungeon, list_locations):

    """ Действия при наличии локаций """
    for number, location in list_locations:
        print(f' - Вход в локацию: - {number} - {location}')

    print(f'Выберите действие:\n'
          f'1.Перейти в другую локацию\n'
          f'2.Сдаться и выйти из игры\n')

    chosen_action = input(f'Ваш выбор: ')

    # проверяем, что введено число
    try:
        chosen_action = int(chosen_action)
    except:
        print(f'ТРЕБУЕТСЯ ВВЕСТИ ЗНАЧЕНИЕ ИЗ ПРЕДЛОЖЕННЫХ!')
        locations(dungeon,list_locations)

    # переход в другую локацию
    if int(chosen_action) == 1:
        # если монстров нет и решил сменить локацию
        dungeon = change_location(dungeon=dungeon, list_locations=list_locations)
        main_game(dungeon=dungeon)

    # сдаться и выйти из игры
    elif int(chosen_action) == 2:
        print(f'Не хватило духу доиграть..Эх,ты!')
        exit()



def main_game(dungeon):
    game_over(dungeon=dungeon)
    # получение списков монстров и локаций
    list_monsters, list_locations = monsters_locations_lists(value_dungeon=dungeon)

    print(f'Внутри вы видите:')

    # если есть монстры и локации
    if list_monsters and list_locations:
        monsters_with_locations(dungeon=dungeon, list_monsters=list_monsters, list_locations=list_locations)

    # если есть монстры, но нет локаций
    elif list_monsters and not list_locations:
        monsters(dungeon=dungeon, list_monsters=list_monsters)

    # если монстров нет
    else:
        locations(dungeon=dungeon, list_locations=list_locations)


if __name__ == '__main__':
    current_location = 0
    current_remaining_time = Decimal(remaining_time)
    counter_location = 0
    counter_monster = 0
    list_locations = []
    list_monsters = []
    experience = 0
    hatch_closed = False
    winner_flag = False
    current_date = 0
    start = time.monotonic()

    for key in dungeon.keys():
        elapsed = time.monotonic() - start
        elapsed = (f'{elapsed: 1.0f}')
        current_date = elapsed

        number_location, time_location = parcing_location_time(chosen_location=key)

        print(f'Вы находитесь в локации - {key}\n'
              f'У вас {experience} опыта и осталось {current_remaining_time} секунд до наводнения\n'
              f'Времени прошло {elapsed} сек\n')

        # логирование в csv локации
        one_more_location = {'current_location': number_location, 'current_experience': experience,
                             'current_date': elapsed}
        with open('dungeon.csv', 'a', newline='') as out_csv:
            writer = csv.DictWriter(out_csv, delimiter=',', fieldnames=field_names)
            writer.writerow(one_more_location)

        dungeon = dungeon[key]

        list_monsters, list_locations = monsters_locations_lists(value_dungeon=dungeon)

        print(f'Внутри вы видите:')

        if list_monsters:

            monsters_with_locations(dungeon=dungeon, list_monsters=list_monsters, list_locations=list_locations)

        else:

            locations(dungeon=dungeon, list_locations=list_locations)

# Учитывая время и опыт, не забывайте о точности вычислений!
