"""
    используем наш обработчик вместо стандартного StreamHandler 
    в конфигурационном файле
"""


import os

from my_streamhandler import MyStreamHandler


log_dir = os.path.join(os.path.dirname(__file__), 'log_file.log')

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'formatter': {
            'format': '%(name)s | %(levelname)s | %(message)s | %(module)s,%(funcName)s:%(lineno)d'
        }
    },

    'handlers': {}
}