"""
Напишите функцию, которая с помощью subprocess будет запускать команду:
$ curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json
- Токенизируйте через shlex, 
- распарсите вывод и 
- верните строку — IP-адрес.

"""


import shlex
import subprocess
import sys


def get_ip_address():
    command = 'curl -i -H "Accept: application/json" -X GET https://api.ipify.org?format=json'

    # токенизация команды:
    args = shlex.split(command)

    # выполнение команды:
    result = subprocess.run(args, )





    print(result)

if __name__ == '__main__':
    get_ip_address()
