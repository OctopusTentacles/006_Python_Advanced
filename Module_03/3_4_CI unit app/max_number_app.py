""" Test for app MAX_NUMBER """


from flask import Flask


app = Flask(__name__)


@app.route('/max_number/<path:numbers>')
def max_number(numbers: str):
    numbers_as_num = (int(num) for num in numbers.split('/'))
    return f'Максимальное число: <i>{max(numbers_as_num)}</i>'


if __name__ == '__main__':
    app.run(debug=True)