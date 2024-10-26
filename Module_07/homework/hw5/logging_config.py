import logging
import logging.config
import os

from logging.handlers import TimedRotatingFileHandler


log_dir = os.path.join(os.path.dirname(__file__), 'logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'base': {
            'format': '%(levelname)-8s || %(name)-10s || %(asctime)s || line %(lineno)-4d || %(message)s'
        }
    },

    'handlers': {
        'rotating_handler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'utils.log'),
            'when': 'S',
            'interval': 10,
            'backupCount': 2,
            'encoding': 'utf8'
        },
    },

    'loggers': {
        'utils': {
            'level': 'INFO',
            'handlers': ['rotating_handler'],
            'propagate': False,
        }
    }
}
