import re

from typing import Any, Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data is None:
            return
        msg = message or f'Number must be 10 digits long.'
        if not (min <= len(str(field.data)) <= max):
            raise ValidationError(msg)
    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if field.data is None:
            return
        if not (self.min <= len(str(field.data)) <= self.max):
            if self.message is None:
                self.message = f'Number must be 10 digits long.'
            raise ValidationError(self.message)

# ===================================================================
def name_valid(message: Optional[str] = None):
    def _name_valid(form: FlaskForm, field: Field):
        if field.data is None:
            return
        msg = message or f'Invalid name format. Example: Иванов И.И.'
        pattern = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ]\. [А-ЯЁ]\.$'
        if not re.match(pattern, field.data):
            raise ValidationError(msg)
    return _name_valid

# ===================================================================
def index_valid(index_length: int, message: Optional[str] = None):
    def _index_valid(form: FlaskForm, field: Field):
        if field.data is None:
            return
        msg = message or f'Index must be {index_length} digits long!'
        if not (index_length == len(str(field.data))):
            raise ValidationError(msg)
    return _index_valid

