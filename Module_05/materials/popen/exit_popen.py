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
    token_command = shlex.split(command) #['sleep', '10', '&&', 'exit', '1']

    sleep_command = token_command[:2]
    exit_command = token_command[3:]

    # запуск sleep:
    sleep_processes = subprocess.Popen(sleep_command)
    # ожидание завершения sleep:
    sleep_processes.wait()

    exit_process = 1

    
    return exit_process


if __name__ == '__main__':
    exit_code = sleep_exit()
    print(f'Process exited with code {exit_code}')
