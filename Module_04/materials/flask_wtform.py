from flask import Flask, request
from flask_wtform import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange



app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    address = StringField()
    index = IntegerField()
    comment = StringField()


@app.route('/registration', methods=['POST'])
def registration():
    form_data = request.get_data(as_text=True)


    print(f'Form data = {form_data}')

    return 'Ok'


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)