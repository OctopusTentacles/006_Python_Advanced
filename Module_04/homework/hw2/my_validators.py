from typing import Any, Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data is None:
            return
        if not (min <= len(str(field.data)) <= max):
            if message is None:
                message = f'Number must be between {min} and {max} digits long.'
            raise ValidationError(message)
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
                self.message = f'Number must be between {self.min} and {self.max} digits long.'
            raise ValidationError(self.message)
