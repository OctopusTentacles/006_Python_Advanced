import configparser
import os


def ini_to_dict(ini_file_path):
    """
    Конвертирует INI-файл в словарь.
    
    Args:
        ini_file_path (str): Путь к INI-файлу.
    
    Returns:
        dict: Конфигурация в формате словаря.
    """

    file_path = os.path.join(os.path.dirname(__file__), ini_file_path)

    config = configparser.ConfigParser()
    config.read(file_path)