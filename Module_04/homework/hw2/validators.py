from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field


def number_length(min: int, max: int, message: Optional[str] = None):
    ...


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        ...