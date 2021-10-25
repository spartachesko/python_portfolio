# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...

from district.central_street.house1.room1 import folks as f_1
# из дома 1 комната 2
from district.central_street.house1.room2 import folks as f_2
# из дома 2 комната 1
from district.central_street.house2.room1 import folks as f_3
# из дома 2 комната 2
from district.central_street.house2.room2 import folks as f_4
# импорт соседей с советской улицы
# из дома 1 команата 1
from district.soviet_street.house1.room1 import folks as f_5
# из дома 1 комната 2
from district.soviet_street.house1.room2 import folks as f_6
# из дома 2 комната 1
from district.soviet_street.house2.room1 import folks as f_7
# из дома 2 комната 2
from district.soviet_street.house2.room2 import folks as f_8

all_citizens = f_1 + f_2 + f_3 + f_4 + f_5 + f_6 + f_7 + f_8
print("На районе живут ", ', '.join(all_citizens))

