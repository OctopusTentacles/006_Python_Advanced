import logging
import sys

from utils import string_to_operator


# функция конфигурирования логирования:
def logging_config():
    # handler stdout:
    handler = logging.StreamHandler(sys.stdout)

    # formatter:
    formatter = logging.Formatter(
        fmt='%(levelname)s | %(name)s | %(asctime)s | line %(lineno)d | %(message)s'
    )
    # добавить форматирование к обработчикам:
    handler.setFormatter(formatter)

    # config:
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler]
    )

# logging:
logging_config()
logger = logging.getLogger('arithmetic_logger')


def calc(args):
    logger.info(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.error("Error while converting number 1")
        logger.debug(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.error("Error while converting number 2")
        logger.debug(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    logger.info(f"Result: {result}")
    logger.info(f"{num_1} {operator} {num_2} = {result}")


if __name__ == '__main__':
    # calc(sys.argv[1:])
    calc('2+3')