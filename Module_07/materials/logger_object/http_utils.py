import logging
import time

import requests


# настройка логгера logger_utils и его дочерних логгеров:
logger_utils = logging.getLogger('logger_utils')
logger_http_utils = logging.getLogger('logger_utils.http_utils')

# уровень логирования для родителя:
logger_utils.setLevel('INFO')

GET_IP_URL = 'https://api.ipify.org?format=json'


def get_ip_address() -> str:
    logger_http_utils.debug('Start getting IP address')
    start = time.time()
    try:
        ip = requests.get(GET_IP_URL).json()['ip']
    except Exception as e:
        logger_http_utils.exception(e)
        raise e
    logger_http_utils.debug('Done requesting ip in {:.4f} seconds'.format(time.time() - start))
    logger_http_utils.info('Ip address: {}'.format(ip))
    return ip
