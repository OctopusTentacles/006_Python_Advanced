from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField



app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
    index = IntegerField()
    comment = StringField()


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