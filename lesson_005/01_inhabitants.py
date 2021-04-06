# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# здесь ваш код

from room_1 import folks as folks_1
from room_2 import folks as folks_2
first_person = folks_1[0]
second_person = folks_1[1]
third_person = folks_2[0]
print("В комнате room_1 живут ", first_person, " и ", second_person)
print("В комнате room_2 живут ", third_person)
