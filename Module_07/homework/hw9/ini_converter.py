import configparser


def ini_to_dict(ini_file_path):
    """
    Конвертирует INI-файл в словарь.
    
    Args:
        ini_file_path (str): Путь к INI-файлу.
    
    Returns:
        dict: Конфигурация в формате словаря.
    """
    