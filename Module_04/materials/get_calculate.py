from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/calculate/', methods=['GET'])
def calculate():
    ...



if __name__ == '__main__':
    app.run(debug=True)