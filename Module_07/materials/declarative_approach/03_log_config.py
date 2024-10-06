
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
        }
    },

    'loggers': {
        '': { # root logger
            'level': 'DEBUG',
            'handlers': ['root_handler'],
        },
        'sub_1': {
            'level': 'INFO',
            'handlers': ['root_handler'],
        },
        'sub_2': {
            # 'level': 'DEBUG', # наследует от root
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
