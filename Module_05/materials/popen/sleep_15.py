"""
Запустите с помощью объекта Popen команду:
$ sleep 15 && echo "My mission is done here!"
Запустите сразу десять таких объектов так, 
чтобы всё вместе это заняло примерно 15 секунд, но не более 20.
"""


import shlex
import subprocess
import time


def all_sleep():
    command = "sleep 15 && echo 'My mission is done here!'"

    # токенизация команды:
    token_command = shlex.split(command)
    # print(token_command) ['sleep', '15', '&&', 'echo', 'My mission is done here!']

    sleep_token_command = token_command[:2]
    echo_token_command = token_command[3:]

    # запуск 10 sleep:
    sleep_processes = [
        subprocess.Popen(
            sleep_token_command,
            stdout=subprocess.PIPE,
            text=True
        )
        for _ in range(10)
    ]
    # ожидание завершения всех sleep:
    for process in sleep_processes:
        process.wait()
    
    # запуск 10 echo:
    echo_processes = [
        subprocess.Popen(
            echo_token_command,
            stdout=subprocess.PIPE,
            text=True
        )
    ]
    # завершение и вывод:
    for process in echo_processes:
        process.wait()
        print(process.stdout())







    # запуск 10 процессов:
    # result = [
    #     subprocess.Popen(
    #         command,
    #         shell=True,
    #         stdout=subprocess.PIPE,
    #         text=True
    #     )
    #     for _ in range(10)
    # ]



if __name__ == '__main__':
    start_time = time.time()
    all_sleep()
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time} sec.')
