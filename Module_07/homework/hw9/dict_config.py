# TODO переписать реализацию ini-файла в формате dict-конфигурации.

{
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler'],
        },
        'appLogger': {
            'level': 'DEBUG',
            'handlers': ['consoleHandler', 'fileHandler'],
            'qualname': 'appLogger',
            'propagate': False,
        },
    },

    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'consoleFormatter',
            'stream': 'ext://sys.stdout',
        },
        'fileHandler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'fileFormatter',
            'filename': 'logfile.log',
        },
    },

    'formatters': {
        'fileFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z',
        },
        'consoleFormatter': {
            'format': '%(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%Z',
        },
    },
}