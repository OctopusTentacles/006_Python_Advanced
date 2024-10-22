import logging
import os


log_dir = os.path.join(os.path.dirname(__file__), 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'base': {
            'format': '%(levelname)s || %(name)s || %(asctime)s || line %(lineno)d || %(message)s'
        }
    },

    'handlers': {
        'file_handler': {
            'class': 'logger_helper.LevelFileHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'base_filename': os.path.join(log_dir, 'calc')
        },
    },

    'loggers': {
        'arithmetic_logger': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
            # отключить передачу логов выше,
            # устранить дублирование логов:
            'propagate': False,
        },
        'operators_logger': {
            'level': 'DEBUG',
            'handlers': ['file_handler'],
            # отключить передачу логов выше,
            # устранить дублирование логов:
            'propagate': False,

        }
    },
}
