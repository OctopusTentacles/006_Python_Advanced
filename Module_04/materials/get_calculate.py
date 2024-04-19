from flask import Flask, request, jsonify
from typing import List, Optional


app = Flask(__name__)


@app.route('/calculate', methods=['GET'])
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
    
    # Проверка наличия хотя бы одного числа в массиве:
    if not numbers:
        return jsonify({'error': 'Empty list. Please provide at least one number.'}), 400
    
    # Вычисление суммы и произведения чисел:
    sum_numbers = sum(numbers)

    product_numbers = 1
    for num in numbers:
        product_numbers *= num
    
    return jsonify({
        'sum': sum_numbers,
        'product': product_numbers
    })


if __name__ == '__main__':
    app.run(debug=True)