import subprocess, sys


def run_program():
    res = subprocess.run(
        ['python', 'test_program.py'], 
        input=b'some input\notherinput',
        # захват потоков:
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # Объединяем stdout и stderr и выводим в stderr:
    output = res.stdout + res.stderr

    # перенаправить весь объединенный вывод в stderr:
    print(output, file=sys.stderr)


if __name__ == '__main__':
    run_program()

