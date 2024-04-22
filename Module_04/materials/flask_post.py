import json
from urllib.parse import unquote_plus

from flask import Flask, request


app = Flask(__name__)


# form_data:
@app.route('/sum', methods=['POST'])
def _sum():
    array1 = request.form.getlist('array1', type=int)
    array2 = request.form.getlist('array2', type=int)

    result = ','.join(str(a1 + a2) for (a1, a2) in zip(array1, array2))

    return f'Array of sums is: [{result}]'


# urlencoded:
@app.route('/sum2', methods=['POST'])
def _sum2():
    form_data = request.get_data(as_text=True)
    request_data = unquote_plus(form_data)

    arrays = {}

    for encoded_chunk in request_data.split('&'):
        key, values = encoded_chunk.split('=')
        arrays[key] = [int(value) for value in values.split(',')]

    result_str = ','.join(
        str(a1 + a2) for (a1, a2) in zip(arrays['array1'], arrays['array2'])
    )

    return f'Your result is {result_str}'


# raw   json:
@app.route('/sum3', methods=['POST'])
def _sum3():
    form_data = request.get_data(as_text=True)

    data_object = json.loads(form_data)

    result_str = ','.join(
        str(a1 + a2) for (a1, a2) in zip(data_object['array1'], data_object['array2'])
    )

    return f'Your result is {result_str}'



if __name__ == '__main__':
    app.run(debug=True)