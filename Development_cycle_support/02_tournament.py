# -*- coding: utf-8 -*-
import argparse
from bowling import get_score
from parcing_tournament import main_start_parcing


# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>



def check_arguments():
    parser = argparse.ArgumentParser(description=f'Обрабатывает протокол турнира и выдает результат')
    parser.add_argument("--input", help="файл протокола турнира")
    parser.add_argument("--output", help="файл результатов турнира")
    parser.add_argument("--market", help="Если подсчет очков требуется для внешнего рынка - укажите"
                                         " new.")
    args = parser.parse_args()
    input_data = args.input
    output_data = args.output
    market_data = args.market
    return input_data, output_data, market_data


if __name__ == "__main__":
    dir_before, dir_after, choosen_market = check_arguments()
    main_start_parcing(directory=dir_before, file_out=dir_after, market=choosen_market)

# game_result = check_arguments()
# result_score = get_score(game_result=game_result)
# print(f'{game_result} - {result_score}')

