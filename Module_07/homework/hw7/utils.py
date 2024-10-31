import logging
import logging.config

from typing import Union, Callable
from operator import sub, mul, truediv, add
from logging_config import dict_config


logging.config.dictConfig(dict_config)
logger_operator = logging.getLogger('operators_logger')
logger_utils = logging.getLogger('utils')

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        logger_operator.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger_operator.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")


    logger_utils.debug("This is a debug message")
    logger_utils.info("This is an info message")
    logger_utils.warning("This is a warning message")
    logger_utils.error("This is an error message")
    logger_utils.critical("This is a critical message")


    return OPERATORS[value]
