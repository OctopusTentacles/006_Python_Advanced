import configparser
import json
import os
import sys


def ini_to_dict(ini_file):
    """
    Конвертирует INI-файл в словарь.
    
    Args:
        ini_file_path (str): Путь к INI-файлу.
    
    Returns:
        dict: Конфигурация в формате словаря.
    """

    config = configparser.ConfigParser(interpolation=None)
    config.read(ini_file)

    # Преобразуем структуру ConfigParser в словарь
    config_dict = {section: dict(config.items(section)) for section in config.sections()}
   
    # Переработка loggers
    if 'loggers' in config_dict:
        logger_keys = config_dict['loggers']['keys'].split(',')
        config_dict['loggers'] = {
            logger_key.strip(): dict(config.items(f'logger_{logger_key.strip()}'))
            for logger_key in logger_keys
        }

    # Переработка handlers
    if 'handlers' in config_dict:
        handler_keys = config_dict['handlers']['keys'].split(',')
        config_dict['handlers'] = {
            handler_key.strip(): {
                key: (str(value) if key == 'args' else value)
                for key, value in config.items(f'handler_{handler_key.strip()}')
            }
            for handler_key in handler_keys
        }

    # Переработка formatters
    if 'formatters' in config_dict:
        formatter_keys = config_dict['formatters']['keys'].split(',')
        config_dict['formatters'] = {
            formatter_key.strip(): dict(config.items(f'formatter_{formatter_key.strip()}'))
            for formatter_key in formatter_keys
        }

    return config_dict


file_path = os.path.dirname(__file__)


ini_file = 'logging_conf.ini'
output_file = 'logging_config.json'

path_ini_file = os.path.join(file_path, ini_file)
path_output_file = os.path.join(file_path, output_file)

converted_dict = ini_to_dict(path_ini_file)

# Сохраняем словарь в JSON-файл
with open(path_output_file, 'w', encoding='utf-8') as json_file:
    json.dump(converted_dict, json_file, indent=4, ensure_ascii=False)

print(f"Конфигурация сохранена в файл: {output_file}")
