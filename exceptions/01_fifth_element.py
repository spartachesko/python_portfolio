# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
try:
    BRUCE_WILLIS = 42

    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as VaEr:
    print(f'невозможно преобразовать к числу -{VaEr}, параметры {VaEr.args}')
except IndexError as InEr:
    print(f'выход за границы списка-{InEr}, параметры {InEr.args}')
except Exception as exc:
    print(f'Что-то пошло не так - {exc}. Проверь еще раз код.')

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
