import subprocess


def simple_popen():
    process = subprocess.Popen(['python', 'test_programm.py'])
    return process


if __name__ == '__main__':
    res = simple_popen()