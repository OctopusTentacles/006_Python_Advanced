"""
нужно использовать команду ps -A, 
чтобы получить список всех запущенных процессов в системе, 
затем подсчитать их количество и вывести результат в консоль.

1 - Используем subprocess.run для выполнения команды ps -A.
2 - Захватываем стандартный вывод команды.
3 - Подсчитываем количество строк в выводе 
    (каждая строка соответствует одному процессу).
4 - Выводим количество процессов.

"""


import shlex
import subprocess


def count_processes():
    command = 'ps -A'

    # токенизация команды:
    token_command = shlex.split(command)

    # выполнение команды:
    result = subprocess.run(
        token_command,
        stdout=subprocess.PIPE,
        text=True
    )

    # вывод команды:
    output = result.stdout
    # print(output)

    # разбиваем вывод на список строк:
    lines = output.splitlines()

    # Первая строка вывода ps -A — это заголовок таблицы 
    # (например, PID TTY TIME CMD).
    # Поэтому количество процессов равно общему количеству строк 
    # минус одна строка заголовка.
    process_count = len(lines) - 1

    print(f'Total number of processes: {process_count}')


if __name__ == '__main__':
    count_processes()