import subprocess


def run_programm():
    res = subprocess.run(['python', 'test_programm.py'])
    print(res)


if __name__ == '__main__':
    run_programm()