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
    result = subprocess.run(
        args, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )
    
    # Вывод команды
    output = result.stdout
    print(output)

    # Проверка наличия заголовков и тела
    if '\n\n' not in output:
        raise Exception("Invalid response format: missing header-body separator")


    # заголовки :
    # HTTP/2 200 
    # date: Thu, 23 May 2024 17:02:30 GMT
    # content-type: application/json
    # content-length: 20
    # vary: Origin
    # cf-cache-status: DYNAMIC
    # server: cloudflare
    # cf-ray: 88869d2659962bcf-FRA

    # тело:
    # {"ip":"146.23.46.5"}

    # HTTP-ответ состоит из двух частей:
    # Заголовков (Headers): Каждый заголовок заканчивается \n.
    # Тела (Body): Тело ответа следует после заголовков.
    # Для того чтобы отделить заголовки от тела, 
    # используется последовательность \n\n:

    # Один \n завершает последний заголовок.
    # Второй \n указывает, что заголовки закончились и начинается тело.

    # Когда вы используете split('\n\n', 1), 
    # вы говорите Python, что хотите разделить строку на две части:
    # Первая часть будет содержать все заголовки.
    # Вторая часть будет содержать тело ответа.
    headers, body = output.split('\n\n', 1)
    print('\nЗАГОЛОВКИ\n',headers)
    print('\nТЕЛО\n',body)



if __name__ == '__main__':
    get_ip_address()


