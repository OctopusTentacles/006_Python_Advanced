from flask import Flask, request, jsonify
from typing import List


app = Flask(__name__)


@app.route('/massive', methods=['GET'])
def massive():
    # Получение массивов A и B из параметров GET-запроса:
    A = request.args.getlist('A', type=int)
    B = request.args.getlist('B', type=int)

    # Проверка наличия хотя бы одного элемента в каждом массиве:





if __name__ == '__main__':
    app.run(debug=True)