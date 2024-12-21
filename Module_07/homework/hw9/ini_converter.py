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

    # Преобразуем структуру ConfigParser в словарь
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
   
    # Обрабатываем ключи (handlers, formatters и т.д.):
    if 'loggers' in config_dict:
        config_dict['loggers'] = {
            key: {
                subkey: (value.split(',') if ',' in value else value)
                for subkey, value in config.items(key)
            }
            for key in config_dict['loggers']['keys'].split(',')
        }

    if 'handlers' in config_dict:
        config_dict['handlers'] = {
            key: {

            }
            for key in config_dict['handlers']['keys'].split(',')
        }