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
        'file_debug': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'calc_debug.log'),
            'mode': 'a'
        },
        'file_info': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'calc_debug.log'),
            'mode': 'a'
        },
        'file_error': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'calc_error.log'),
            'mode': 'a'
        },
        'file_warning': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'calc_warning.log'),
            'mode': 'a'
        },
        'file_critical': {
            'class': 'logging.FileHandler',
            'level': 'CRITICAL',
            'formatter': 'base',
            'filename': os.path.join(log_dir, 'calc_critical.log'),
            'mode': 'a'
        }
    },

    'loggers': {
        'arithmetic_logger': {
            'level': 'DEBUG',
            'handlers': [
                'file_debug', 'file_info', 'file_error',
                'file_warning', 'file_critical'
            ],
            # отключить передачу логов выше,
            # устранить дублирование логов:
            'propagate': False,
        },
        'operators_logger': {
            'level': 'DEBUG',
            'handlers': [
                'file_debug', 'file_info', 'file_error',
                'file_warning', 'file_critical'
            ],
            # отключить передачу логов выше,
            # устранить дублирование логов:
            'propagate': False,

        }
    },
}
