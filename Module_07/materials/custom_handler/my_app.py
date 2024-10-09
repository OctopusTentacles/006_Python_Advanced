import logging
import logging.config

from my_config import dict_config


# применяем конфигурацию:
logging.config.dictConfig(dict_config)

# определить логгеры:
root = logging.getLogger('root')
sub_1 = logging.getLogger('sub_1')
sub_2 = logging.getLogger('sub_2')
sub_sub_1 = logging.getLogger('sub_1.sub_sub_1')

