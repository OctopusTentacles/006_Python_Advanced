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
    
    # Находим число из массива A, наиболее близкое к числу X:
    closest_number = find_closest_number(A, X)

    return jsonify({'closest number to {X}': closest_number})


def find_closest_number(A: List[int], X: int) -> int:
    closest = A[0]
    min_diff = abs(X - A[0])

    for num in A:
        diff = abs(X - num)
        if diff < min_diff:
            closest = num
            min_diff = diff
    return closest


if __name__ == '__main__':
    app.run(debug=True)