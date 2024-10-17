import os


log_dir = os.path.join(os.path.dirname(__file__), 'logs')

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
        }
    },

    'loggers': {

    },
}