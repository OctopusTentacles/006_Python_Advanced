from flask import Flask, request



app = Flask(__name__)



@app.route('/registration', methods=['POST'])
def registration():
    form_data = request.get_data(as_text=True)


    print(f'Form data = {form_data}')

    return 'Ok'


if __name__ == '__main__':
    app.run(debug=True)