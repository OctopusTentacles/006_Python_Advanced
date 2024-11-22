# TODO переписать реализацию ini-файла в формате dict-конфигурации.

{
    'loggers': {
        'keys': ['root', 'appLogger']
    },

    'handlers': {
        'keys': ['consoleHandler', 'fileHandler']
    },

    'formatters': {
        'keys': ['fileFormatter', 'consoleFormatter']
    },





    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': 'consoleHandler',
        },
        'appLogger': {
            'level': 'DEBUG',
            'handlers': ['consolHandler', 'fileHandler'],
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
            'stream': 'logfile.log',
        },
    },


    'formatters': {
        
    }
}
