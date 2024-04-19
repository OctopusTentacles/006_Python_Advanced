from flask import Flask, request, jsonify
from typing import List


app = Flask(__name__)


@app.route('/massive', methods=['GET'])
def massive():
    ...



if __name__ == '__main__':
    app.run(debug=True)