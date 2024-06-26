from flask import Flask


app = Flask(__name__)

@app.endpoint('test')
def test_endpoint():
    return 'Test endpoint was called!'


if __name__ == '__main__':
    app.run()


# python simple_app.py & - знак амперсента позволяет запускать
# приложение на заднем фоне - [1] 26006 - получаем номер задания и бит процесса.


# python simple_app.py > /dev/null &
# перенаправляем output программы в никуда,
# dev/null - черная дыра.

# jobs - проверить текущие задания

# kill -9 26006 - выключить задание - используем PID и сигнал -9

# запустим задание без лишних выводов - python simple_app.py > /dev/null &

# 3 потока
# 0 - stdin - чтение из (клавиатура, файл)
# 1 - stdout - вывод (print)
# 2 - stderr - вывод диагностических сообщений

# > /dev/null & перенаправляет в никуда только stdout

# python simple_app.py 2>&1 > /dev/null &
# поток 2 перенаправляем в поток 1 (stderr -> stdout)

# приостановка задания (stop) - ctr+z
# для продолжения работы (front ground) - fg



# Перенаправить выходные данные Flask-сервера в файл stdout.txt, 
# а ошибки в stderr.txt: python simple_app.py > stdout.txt 2> stderr.txt &

# Запуск Flask-сервера в фоновом режиме и сохранение PID
# echo $! > flask_pid.txt

# Завершает процесс с указанным PID
# kill $(cat flask_pid.txt)

# Запуск Flask-сервера и сохранение его PID
# python simple_app.py > stdout.txt 2> stderr.txt & echo $! > flask_pid.txt

# Перезапуск Flask-сервера
# kill $(cat flask_pid.txt) && python simple_app.py > stdout.txt 2> stderr.txt & echo $! > flask_pid.txt

# Команда для проверки и создания директории:
# test -d test || mkdir test

# Объединение с запуском Flask-сервера
# test -d my_directory || mkdir my_directory: 
# Проверяет существование директории и создает её, если не существует.
# &&: Если директория существует или была успешно создана, выполняет следующую команду.
# python your_flask_app.py > stdout.txt 2> stderr.txt & echo $! > flask_pid.txt: 
# Запускает Flask-сервер, перенаправляет вывод и ошибки в соответствующие файлы 
# и сохраняет PID процесса в файл flask_pid.txt


# (test -d test || mkdir test) && (python simple_app.py > stdout.txt 2> stderr.txt & echo $! > flask_pid.txt)


# проверка процессов на порте
# lsof -i :5000

# убиить процесс
# kill -9 pid


# Пример полного сценария с перезапуском сервера
# (test -d test || mkdir test) && (kill $(cat flask_pid.txt)) && (python simple_app.py > stdout.txt 2> stderr.txt & echo $! > flask_pid.txt)