"""
В прошлой практике вы уже несколько раз использовали функцию 
subprocess.run. Попробуйте переписать ваш код по запуску команды ps так, 
чтобы вместо функции run у вас был объект Popen.

"""


import shlex
import subprocess


def count_processes():
    command = 'ps -A'

    # токенизация команды:
    token_command = shlex.split(command)

    # выполнение команды:
    result = subprocess.Popen(
        token_command,
        stdout=subprocess.PIPE,
        text=True
    )

    # вывод команды:
    output = result.stdout
    lines = output.splitlines()
    process_count = len(lines) - 1

    return process_count


if __name__ == '__main__':
    res = count_processes()
    print(f'Total number of processes: {res}')
