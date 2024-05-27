"""
Запустите такую команду, используя объект Popen: 
$ sleep 10 && exit 1

"""


import shlex
import subprocess
import time



def sleep_exit():
    command = 'sleep 10 && exit 1'

    # токенизация команды:
    token_command = shlex.split(command)
    print(token_command)



if __name__ == '__main__':
    sleep_exit()