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
    }
}
