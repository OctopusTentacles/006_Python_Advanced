import logging
import flask

from http_utils import get_ip_address
from subprocess_utils import get_kernel_version


# настройка основного логгера (root):
logging.basicConfig(level='DEBUG')

# логгер main с уровнем INFO:
main_logger = logging.getLogger('main')
main_logger.setLevel('INFO')

# логгер utils с уровнем DEBUG:
utils_logger = logging.getLogger('utils')

app = flask.Flask(__name__)


@app.route('/get_system_info')
def get_system_info():
    main_logger.info('Start working')
    ip = get_ip_address()
    kernel = get_kernel_version()
    return "<p>{}</p><p>{}</p>".format(ip, kernel)


if __name__ == '__main__':
    app.run(debug=True)
