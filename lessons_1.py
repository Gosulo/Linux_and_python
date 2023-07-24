# Задание 1.
# Условие:
# аписать функцию на Python, которой передаются в качестве параметров команда и текст.
#  Функция должна возвращать True, если команда успешно выполнена и текст найден в её
# выводе и False в противном случае. Передаваться должна только одна строка,
# разбиение вывода использовать не нужно.

import subprocess


def comand_file(comands):
    comands = input('Введите команту и текст через запятую')
    comand, text = comands.split(',')
    res = subprocess.run(f'{comand} ', shell=True,
                         stdout=subprocess.PIPE, encoding='utf-8')
    if res.returncode == 0:
        if 'VERSION="22.04.2 LTS (Jammy Jellyfish)"' in text and 'VERSION_CODENAME-jammy' in text:
            print('SUCCESS 2.0')
        else:
            print('FAULSE')
    else:
        print('FAULSE')
