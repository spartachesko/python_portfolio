def get_score(game_result, status):
    list_score = []
    list_frame = []
    counter_shoot_in_game = 0
    rules = status
    for shoot in game_result:

        if shoot in 'X,/,1,2,3,4,5,6,7,8,9,-':
            # проверка strike
            if shoot == 'X':
                list_frame = ['X']
                list_score.append(list_frame)
                list_frame = []
                counter_shoot_in_game += 1
                continue

            # проверка на повторяемость и корректность позиционирования spare
            elif shoot == '/':

                list_frame.append('/')

                if list_frame[0] == '/':
                    raise Exception(f'/ находится на первой позиции')


                elif list_frame[0] == list_frame[1]:
                    raise Exception(f'Два раза подряд введен /')

                list_score.append(list_frame)
                list_frame = []

            # проверка промаха
            elif shoot == '-':

                list_frame.append('0')

                # добавление фрейма в общий список
                if len(list_frame) == 2:
                    list_score.append(list_frame)
                    list_frame = []

            # проверка обычных бросков
            else:
                list_frame.append(shoot)

                # Проверка количества бросков во фрейме
                if len(list_frame) == 2:
                    # Проверка количества сбитых кегель в одном фрейме
                    if int(list_frame[0]) + int(list_frame[1]) > 10:
                        raise Exception(f'Количество сбитых в одном фрейме кегель превышает 10')


                    elif int(list_frame[0]) + int(list_frame[1]) == 10:
                        raise Exception(f'Во внесенном формате  сумма сбитых кегель за фрейм не должна '
                                        f'быть равна 10. Если второй бросок сбил оставшиеся кегли, укажите '
                                        f'/')
                    list_score.append(list_frame)
                    list_frame = []

            # Текущий бросок
            counter_shoot_in_game += 1

            # Проверка на минимальное кол-во фреймов
            if len(list_score) > 10:
                raise Exception(f'Количество фреймов больше 10')

            if len(game_result) == counter_shoot_in_game and len(list_score) < 10:
                raise Exception(f'Количество фреймов меньше 10')

        # Проверка на корректность введенного значения
        else:
            raise Exception(f'Некорректно введено значение {shoot}')

    if rules == 'new':
        result = market_global(list_for_calculating=list_score)
    else:
        result = market_local(list_for_calculating=list_score)

    return result


def market_local(list_for_calculating):
    # правило подсчета очков для внутреннего рынка
    result_score = 0
    for frame in list_for_calculating:
        if frame[0] == 'X':
            result_score += 20
        elif frame[1] == '/':
            result_score += 15

        else:
            result_score += int(frame[0]) + int(frame[1])

    return result_score


def market_global(list_for_calculating):
    # правило подсчета очков для внешнего рынка
    result_score = 0
    value_last = 0
    value = 0
    list_for_calculating = list(reversed(list_for_calculating))
    for frame in list_for_calculating:

        value_last_last_last = value_last
        value_last_last = value

        if frame[0] == 'X':
            result_score += 10
            result_score += int(value) + int(value_last_last_last)
            value_last = value
            value = 10

        elif frame[1] == '/':
            result_score += 10
            value_last = 0  # /
            value = int(frame[0])
            result_score += value_last_last

        else:

            result_score += int(frame[0]) + int(frame[1])
            value_last = int(frame[1])
            value = int(frame[0])

    return result_score

