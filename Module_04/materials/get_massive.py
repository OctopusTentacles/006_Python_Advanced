from flask import Flask, request, jsonify
from itertools import product


app = Flask(__name__)


@app.route('/massive', methods=['GET'])
def massive():
    # Получение массивов A и B из параметров GET-запроса:
    A = request.args.getlist('A', type=int)
    B = request.args.getlist('B', type=int)

    # Проверка наличия хотя бы одного элемента в каждом массиве:
    if not A or not B:
        return jsonify({'error': 'Please provide arrays A and B'}), 400
    
    # # Создание всех возможных комбинаций пар чисел из A и B:
    all_combinations = list(product(A, B))

    return jsonify({'combinations': all_combinations})


if __name__ == '__main__':
    app.run(debug=True)