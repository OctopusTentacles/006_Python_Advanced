from typing import Optional

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
