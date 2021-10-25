import copy
import os
from bowling import get_score


def to_parce_doc(path, choosen_market):
    path_normalized = os.path.normpath(path)
    with open(path_normalized, "r") as txt:
        winner_name = '-'
        winner_score = 0
        separator = '  '
        for line in txt:
            line_for_yield = line.rstrip()
            line_tmp = line_for_yield.split()

            if 'Tour' in line_tmp:
                yield line
                continue

            if 'winner' in line_tmp:
                line_tmp.pop(-1)
                line_tmp.append(winner_name)
                line_tmp = separator.join(line_tmp)
                line_tmp = line_tmp + '\n' + '\n'
                yield line_tmp
                winner_score = 0
                winner_name = '-'

                continue
            if len(line_tmp) == 2:

                gamer_name = line_tmp[0]
                gamer_result = line_tmp[1]
                try:
                    quantity_of_score = get_score(game_result=gamer_result, status=choosen_market)
                except Exception as exc:
                    quantity_of_score = 0
                    line = line_for_yield + f'  {exc}\n'
                    yield line
                    continue

                line = line_for_yield + f'    {quantity_of_score}\n'
                yield line
                if quantity_of_score > winner_score:
                    winner_name = copy.copy(gamer_name)
                    winner_score = copy.copy(quantity_of_score)

        return


def main_start_parcing(directory, file_out, market):
    file = open(file_out, mode='w')
    for parced_line in to_parce_doc(path=directory, choosen_market=market):
        file.write(parced_line)
    file.close()

