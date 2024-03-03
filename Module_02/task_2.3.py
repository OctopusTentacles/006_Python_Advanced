# Вызовите команду $ ls -la для папки /etc . Скопируйте output в файл. 
# Обратите внимание: мы опустили флаг -h, который сделал бы формат размера 
# человекачитаемым. Напишите программу, которая бы переработала 
# результат так, будто он был выведен с использованием флага -h

# С помощью python выясните количество файлов и папок в output. 
# У папок права доступа обычно начинаются с d , например drwxr-xr-x. 
# По этому признаку папки можно отличить от файлов.
# Подсчитайте суммарный размер всех файлов в папке /etc в байтах
# Переведите его в человекочитаемый формат 
# (1024 байта = 1 кБ, 1024 кБ = 1 МБ и тд). 
# Напишите функцию, которая по output из ls -la 
# выводит суммарный размер файлов в человекочитаемом формате.


import subprocess


def human_readable_size(size_in_bytes):
    """
    Преобразует размер из байтов в человекочитаемый формат.
    """
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size_in_bytes >= 1024 and index < len(suffixes) - 1:
        size_in_bytes /= 1024.0
        index += 1
    return f"{size_in_bytes:.2f} {suffixes[index]}"


def parse_ls_output(ls_output):
    """
    Парсит вывод команды ls -la и возвращает количество файлов и папок,
    а также суммарный размер всех файлов в папке.
    """
    total_size = 0
    num_files = 0
    num_dirs = 0

    for line in ls_output.split('\n'):
        if line.startswith('d'):
            num_dirs += 1
        else:
            num_files += 1
            fields = line.split()
            if len(fields) > 4:
                try:
                    size = int(fields[4])
                    total_size += size
                except ValueError:
                    pass

    return num_files, num_dirs, total_size


def get_ls_output(directory):
    """
    Выполняет команду ls -la для указанной директории и возвращает ее вывод.
    """
    try:
        result = subprocess.run(
            ['ls', '-la', directory], 
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None