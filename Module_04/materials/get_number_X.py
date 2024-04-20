from flask import Flask, request, jsonify
from typing import List


app = Flask(__name__)


@app.route('/number', methods=['GET'])
def number():
    ...



if __name__ == '__main__':
    app.run(debug=True)