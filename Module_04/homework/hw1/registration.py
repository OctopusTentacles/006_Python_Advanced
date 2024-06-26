from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange, Optional

from .my_validators import number_length, NumberLength, name_valid, index_valid


app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[
        InputRequired(),
        Email(message='Invalid email format')
    ])
    phone = IntegerField(validators=[
        InputRequired(),
        NumberRange(min=1000000000, max=9999999999, message='Phone number must be 10 digits long'),
        number_length(min=10, max=10, message='wrong number length!!!'),
        NumberLength(10, 10, 'WRONG PHONE-NUMBER!!!')
    ])
    name = StringField(validators=[
        InputRequired(message='Name is required!'),
        name_valid()
    ])
    address = StringField(validators=[
        InputRequired(message='Address is required!')
    ])
    index = IntegerField(validators=[
        InputRequired(message='Index is required!'),
        index_valid(index_length=6)
    ])
    comment = StringField(validators=[
        Optional()
    ])


@app.route('/registration_hw1', methods=['POST'])
def registration_hw1():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'Successfully registered user {email} with phone +7{phone}'

    return f'Invalid input, {form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
