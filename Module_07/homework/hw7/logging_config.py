import logging
import logging.config
import os

from contextlib import redirect_stdout
from logging import LogRecord
from logging.handlers import TimedRotatingFileHandler
from logging_tree import printout


log_dir = os.path.join(os.path.dirname(__file__), 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# ===================================================================
# class logging.Filter - базовый класс для создания фильтров логирования.
# def filter() - пропускает все сообщения, возвращая True.
# - создать класс, наследуемый от logging.Filter,
# - настроить метод filter() на проверку не ASCII-символов.
class ASCIIFilter(logging.Filter):
    """Фильтр для отбора сообщений, содержащих только ASCII-символы."""
    def filter(self, record: LogRecord) -> bool:
        """
        Определяет, содержатся ли в сообщении логирования только ASCII-символы.

        Args:
            record (LogRecord): Объект лог-записи, содержащий информацию о сообщении логирования.

        Returns:
            bool: True, если сообщение содержит только ASCII-символы, иначе False.
        """
        return record.getMessage().isascii()
    
# ===================================================================

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'filters': {
        'ascii_filter': {
            '()': 'logging_config.ASCIIFilter'
        }
    },

    'formatters': {
        'base': {
            'format': '%(levelname)-8s || %(name)-10s || %(asctime)s || line %(lineno)-4d || %(message)s'
        }
    },

    'handlers': {
        'file_handler': {
            'class': 'logger_helper.LevelFileHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'base_filename': os.path.join(log_dir, 'calc'),
            'filters': ['ascii_filter'],
        },

        'rotating_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'utils.log'),
            'when': 'S',
            'interval': 10,
            'backupCount': 2,
            'encoding': 'utf8',
            'filters': ['ascii_filter'],
        },
    },

    'loggers': {
        'arithmetic_logger': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
            'propagate': False,
        },
        'operators_logger': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
            'propagate': False,
        },
        'utils': {
            'level': 'INFO',
            'handlers': ['rotating_handler'],
            'propagate': False,
        }
    }
}

# настройка логгеров, иначе в дереве видно только root:
logging.config.dictConfig(dict_config)
# ===================================================================
# файл для структуры логгеров:
with open(os.path.join(log_dir, 'logging_tree.txt'), 'w') as file:
    with redirect_stdout(file):
        # func printout выводит дерево логов:
        printout()
# ===================================================================
