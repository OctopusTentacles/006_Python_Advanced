import configparser
import json
import os


def ini_to_dict(ini_file_name):
    """
    Конвертирует INI-файл в словарь.
    
    Args:
        ini_file_path (str): Путь к INI-файлу.
    
    Returns:
        dict: Конфигурация в формате словаря.
    """

    file_path = os.path.join(os.path.dirname(__file__), ini_file_name)

    config = configparser.ConfigParser(interpolation=None)
    config.read(file_path)

    # Преобразуем структуру ConfigParser в словарь
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
   
    # Переработка loggers
    if 'loggers' in config_dict:
        logger_keys = config_dict['loggers']['keys'].split(',')
        config_dict['loggers'] = {
            logger_key.strip(): dict(config.items(f'logger_{logger_key.strip()}'))
            for logger_key in logger_keys
        }

    if 'handlers' in config_dict:
        config_dict['handlers'] = {
            key: {
                subkey: (value if subkey != 'args' else eval(value))
                for subkey, value in config.items(key)            }
            for key in config_dict['handlers']['keys'].split(',')
        }
    
    if 'formatters' in config_dict:
        config_dict['formatters'] = {
            key: dict(config.items(key))
            for key in config_dict['formatters']['keys'].split(',')
        }

    return config_dict

ini_file = 'logging_conf.ini'
output_file = 'logging_config.json'

converted_dict = ini_to_dict(ini_file)

# Сохраняем словарь в JSON-файл
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(converted_dict, json_file, indent=4, ensure_ascii=False)

print(f"Конфигурация сохранена в файл: {output_file}")
