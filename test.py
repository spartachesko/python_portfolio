import random
from urllib import urlopen
import sys
WORD_URL = 'http://learncodethehardway.org/words.txt'
WORDS = []

PHRASES = {
    "class %%%(%%%):":
    "Создается класс с именем %%%, наследующим.",
    "class %%%(object):\n\tdef __init__ (self, ***)":
    "Класс %%% комбинирует __init__ с параметрами self, ***.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "Класс %%% комбинирует функцию с именем *** с параметрами self,@@@."
    "*** = %%%()":"Из "
    }