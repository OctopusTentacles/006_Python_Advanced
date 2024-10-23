import logging
import logging.config

from typing import Union, Callable
from operator import sub, mul, truediv, add
from logging_config import dict_config


logging.config.dictConfig(dict_config)
logger = logging.getLogger('operators_logger')

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
        logger.error(f"wrong operator type {value}")
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.error(f"wrong operator value {value}")
        raise ValueError("wrong operator value")
    
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")


    return OPERATORS[value]
