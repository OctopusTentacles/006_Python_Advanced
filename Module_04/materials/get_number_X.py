from flask import Flask, request, jsonify
from typing import List


app = Flask(__name__)


@app.route('/number', methods=['GET'])
def number():
    # получаем отсортированный массив из чисел и число:
    A: List[int] = sorted(request.args.get('A'))
    X: int = int(request.args.get('X'))

    # Проверяем, что массив A и число X были предоставлены:
    if not A or X is None:
        return jsonify({'error': 'Please provide array A and a number X'}), 400
    ...



if __name__ == '__main__':
    app.run(debug=True)