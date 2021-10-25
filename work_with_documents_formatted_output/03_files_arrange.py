# -*- coding: utf-8 -*-

import os
import time
import shutil


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#


class AnalyzePath:

    def __init__(self, file_for_scan):
        self.file_for_scan = file_for_scan

    def checking_files(self, file_for_scan):
        for dirpath, dirnames, filenames in os.walk(file_for_scan):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                year = file_time[0]
                year = str(year)
                self.copy_files(year=year, full_file_path=full_file_path)

    def copy_files(self, year, full_file_path):
        full_target_path = os.path.join(target_path, year)
        if os.path.exists(full_target_path):
            shutil.copy2(full_file_path, full_target_path)

        else:
            os.makedirs(full_target_path)
            shutil.copy2(full_file_path, full_target_path)


analyze_path = 'icons'
target_path = 'icons_by_year'
path_normalized = os.path.normpath(analyze_path)
dir_analyze = AnalyzePath(file_for_scan=path_normalized)
dir_analyze.checking_files(file_for_scan=path_normalized)
