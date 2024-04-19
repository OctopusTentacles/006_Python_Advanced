from flask import Flask, request, jsonify
from typing import List, Optional


app = Flask(__name__)


@app.route('/calculate/', methods=['GET'])
def calculate():
    # Получение чисел из параметра запроса:
    numbers_str:  List[str] = request.args.get('numbers')
    if not numbers_str:
        return jsonify({'error': 'Please provide a list of numbers.'}), 400
    
    # преобразуем строку в список чисел:
    try:
        numbers = [int(num) for num in numbers_str.split(',')]
    except ValueError:
        return jsonify({'error': 'Invalid input. Please provide a list of integers.'}), 400
    ...



if __name__ == '__main__':
    app.run(debug=True)