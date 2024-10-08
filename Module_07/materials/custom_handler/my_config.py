"""
    используем наш обработчик вместо стандартного StreamHandler 
    в конфигурационном файле
"""


import os

from my_streamhandler import MyStreamHandler


log_dir = os.path.join(os.path.dirname(__file__), 'log_file.log')