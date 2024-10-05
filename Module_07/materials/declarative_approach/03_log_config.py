
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

    },

    # 'filters': {},
    # 'root': {} # == '': {}
}