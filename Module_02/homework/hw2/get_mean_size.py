"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    print(ls_output)

    total_memory = 0
    count = 0

    for line in ls_output:
        columns = line.split()
        total_memory += int(columns[4])
        count += 1

    return total_memory / count

if __name__ == '__main__':
    data: str = sys.stdin.readlines()[1:]
    mean_size: float = get_mean_size(data)
    print(mean_size)
