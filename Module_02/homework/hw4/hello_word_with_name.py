"""
Реализуйте endpoint /hello-world/<имя>, 
который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать 
хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""


import sys


from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route('/hello-world/<username>')
def hello_world(username):

    weekday = datetime.today().weekday()
    print(weekday)

    weekdays_tuple = (
        'Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды',
        'Хорошего четверга', 'Хорошей пятницы', 'Хорошей субботы',
        'Хорошего воскресения'
    )
    weekdays_list = [
        'Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды',
        'Хорошего четверга', 'Хорошей пятницы', 'Хорошей субботы',
        'Хорошего воскресения'
    ]
    weekdays_dict = {
        0:'Хорошего понедельника', 1:'Хорошего вторника', 2:'Хорошей среды',
        3:'Хорошего четверга', 4:'Хорошей пятницы', 5:'Хорошей субботы',
        6:'Хорошего воскресения'
    }
    
    print(sys.getsizeof(weekdays_tuple))
    print(sys.getsizeof(weekdays_list))
    print(sys.getsizeof(weekdays_dict))

    return f'Привет, {username}. {weekdays_tuple[weekday]}!'


if __name__ == '__main__':
    app.run(debug=True)
