
dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'formatter': {
            'format': '%(name)s || %(levelname)s || %(message)s || %(module)s,%(funcName)s:%(lineno)d'
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
        'sub_1': {
            'level': 'INFO',
            'handlers': [],
        },
        'sub_2': {
            'level': '',
            'propagate': 'FALSE'
        },
        'sub_sub_1': {
            'level': 'DEBUG',
        }
    },

    # 'filters': {},
    # 'root': {} # == '': {}
}