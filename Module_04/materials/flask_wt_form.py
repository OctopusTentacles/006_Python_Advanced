from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, Optional, Regexp, ValidationError



app = Flask(__name__)



def validate_phone(form, field):
    if not str(field.data).isdigit() or len(str(field.data)) != 10:
        raise ValidationError('Invalid phone number')

def validate_index(form, field):
    if field.data is not None and not str(field.data).isdigit():
        raise ValidationError('Index must consist of digits only')
    


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[
        InputRequired(), 
        validate_phone,
        NumberRange(min=1000000000, max=9999999999, message='Invalid phone number'),
    ])
    name = StringField(validators=[
        InputRequired(),
        Regexp(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ]\. [А-ЯЁ]\.$', message='Invalid name format. Example: Иванов И.И.')
    ])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[
        Optional(), 
        validate_index,
        NumberRange(min=000000, max=999999, message='Index must be a positive integer'),
        # Regexp('^[0-9]*$', message='Index must consist of digits only')
    ])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Successfully registered user {email} with phone +7{phone}'
    else:
        errors = form.errors
        return f'Invalid input, {errors}', 400



def is_licky_ticket(ticket_number):
    first_half = sum(int(digit) for digit in str(ticket_number // 1000))
    second_half = sum(int(digit) for digit in str(ticket_number % 1000))
    return first_half == second_half

@app.route()


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
