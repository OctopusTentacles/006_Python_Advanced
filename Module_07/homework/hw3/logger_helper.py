import logging
import os
import sys


class LevelFileHandler(logging.Handler):
    def __init__(self, base_filename):
        super().__init__()
        self.base_filename = base_filename
        self.handlers = {}

        # определить имя файла в зависимости от уровня:
        for level in [
            logging.DEBUG,
            logging.INFO,
            logging.WARNING,
            logging.ERROR,
            logging.CRITICAL
        ]:
            level_name = logging.getLevelName(level).lower()
            # имя файла логирования типа calc + _ + debug + .log:
            filename = f'{self.base_filename}_{level_name}.log'

            # обработчик с выводом потока в файл:
            log_dir = os.path.join(os.path.dirname(__file__), filename)
            handler = logging.FileHandler(log_dir)

            # форматирование логов:


def get_logger(name):
    ...
    return logger

