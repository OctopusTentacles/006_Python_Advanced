import subprocess


def run_programm():
    result = subprocess.run(
        ['python', 'test_programm.py'], 
        input=b'some input\notherinput'
    )

    print(result)


if __name__ == '__main__':
    run_programm()