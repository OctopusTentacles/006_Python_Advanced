"""
Удобно направлять результат выполнения команды напрямую в программу 
с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает 
результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""


import sys


def get_mean_size(ls_output: str) -> float:

    total_memory = 0
    count_files = 0

    for line in ls_output:
        # учитываем только файлы:
        if line.startswith('-'):
            columns = line.split()
            total_memory += int(columns[4])
            count_files += 1

    # на пустой директории - ZeroDivisionError;
    # поэтому добавим условие:
    return total_memory / count_files if count_files > 0 else 0

if __name__ == '__main__':
    data: str = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(data)
    print(mean_size)
