from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, NumberRange, Length, Optional



app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[
        InputRequired(),
        Email(message='Invalid email format')
    ])
    phone = IntegerField(validators=[
        InputRequired(),
        Length(min=10, max=10, message='Phone number must be 10 digits long'),
        NumberRange(min=0, message='Phone number must be positive')
    ])
    name = StringField(validators=[
        InputRequired(message='Name is required!')
    ])
    address = StringField(validators=[
        InputRequired(message='Address is required!')
    ])
    index = IntegerField(validators=[
        InputRequired(message='Index is required!')
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