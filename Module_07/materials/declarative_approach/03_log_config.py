import os


log_dir = os.path.join(os.path.dirname(__file__), 'log_file.log')
dict_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'formatter': {
            'format': '%(name)s || %(levelname)s || %(message)s ||\
                  %(module)s,%(funcName)s:%(lineno)d'
        }
    },

    'handlers': {
        'root_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'formatter'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'formatter',
            'filename': log_dir,
            'mode': 'a'
        },
    },

    'loggers': {
        '': { # root logger
            'level': 'DEBUG',
            'handlers': ['root_handler'],
        },
        'sub_1': {
            'level': 'INFO',
            'handlers': ['root_handler', 'file_handler'],
        },
        'sub_2': {
            # 'level': 'DEBUG', # наследует от root
            'handlers': ['file_handler'],
            'propagate': False
        },
        'sub_sub_1': {
            'level': 'DEBUG',
            'handlers': ['root_handler'],
        }
    },

    # 'filters': {},
    # 'root': {} # == '': {}
}
