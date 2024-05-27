"""
Запустите такую команду, используя объект Popen: 
$ sleep 10 && exit 1


Попробуйте:
Подождать объект девять секунд и проверить, что он не был завершён. 
Чтобы это сделать, вам нужно будет передать в метод wait тайм-аут
https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait.
Подождать без тайм-аута и проверить, что программа вернула код 1.

"""


import shlex
import subprocess
import time



def sleep_exit():
    command = 'sleep 10 && exit 1'

    # токенизация команды:
    token_command = shlex.split(command) #['sleep', '10', '&&', 'exit', '1']

    # sleep_command = token_command[:2]
    # exit_command = token_command[3:]

    # запуск sleep:
    process = subprocess.Popen(token_command, shell=True)
    # ожидание завершения sleep:
    process.wait()

    exit_process = 1

    return_code = process.returncode

    print(f'Process finished with return code: {return_code}')


if __name__ == '__main__':
    start_time = time.time()
    sleep_exit()
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time} sec.')
