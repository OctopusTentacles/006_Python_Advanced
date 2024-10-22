import logging
import os


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

            handler = logging.FileHandler(filename)

            self.handlers[level] = handler
        
    def emit(self, record):
        """
        метод проверяет, есть ли обработчик для уровня логов, 
        и использует его для записи сообщения в определенный
        файл, в зависимости от уровня.

        Args:
            record (LogRecord): объект, содержащий все необходимые 
            данные о текущем лог-сообщении.
        """
        log_level = record.levelno
        handler = self.handlers.get(log_level)

        # запись лога в файл через нужный обработчик:
        if handler:
            formatter = logging.Formatter(
                '%(levelname)s || %(name)s || %(asctime)s || line %(lineno)d || %(message)s'
            )
            handler.setFormatter(formatter)
            handler.emit(record)
        


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # добавляем LevelFileHandler:
    handler = LevelFileHandler(base_filename='calc')
    logger.addHandler(handler)

    return logger

