"""
Запустите с помощью объекта Popen команду:
$ sleep 15 && echo "My mission is done here!"
Запустите сразу десять таких объектов так, 
чтобы всё вместе это заняло примерно 15 секунд, но не более 20.
"""


import shlex
import subprocess


def all_sleep():
    command = 'sleep 15 && echo "My mission is done here!"'

    # токенизация команды:
    token_command = shlex.split(command)

    # выполнение команды:
    result = subprocess.Popen(
        token_command,
        stdout=subprocess.PIPE,
        text=True
    )
    stdout, _ = result.communicate()

    return stdout


if __name__ == '__main__':
    print('Start!')
    res = all_sleep()
