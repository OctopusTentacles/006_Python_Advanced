import logging
import os


class LevelFileHandler(logging.Handler):
    def __init__(self, base_filename, formatter=None):
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

            if formatter:
                handler.setFormatter(formatter)

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
        handler = self.handlers.get(record.levelno)

        # запись лога в файл через нужный обработчик:
        if handler:
            handler.emit(record)
        

    def setFormatter(self, formatter):
        """
        Применяем форматтер ко всем обработчикам внутри LevelFileHandler.
        """
        for handler in self.handlers.values():
            handler.setFormatter(formatter)
