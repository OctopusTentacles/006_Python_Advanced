
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
            'filename': '',
            'mode': 'a'
        }
    },

    'loggers': {

    },
}