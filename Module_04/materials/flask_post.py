import json
from urllib.parse import unquote_plus

from flask import Flask, request


app = Flask(__name__)


@app.route('/sum', methods=['POST'])
def _sum():
    array1 = request.form.getlist('array1', type=int)
    array2 = request.form.getlist('array2', type=int)

    result = ','.join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f'Array of sums is: [{result}]'


@app.route('/sum2', methods=['POST'])
def _sum2():
    form_data = request.get.data(as_text=True)
    print(f'form_data = {form_data}')

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)