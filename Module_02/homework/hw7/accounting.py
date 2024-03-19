"""
Реализуйте приложение для учёта финансов, умеющее запоминать, 
сколько денег было потрачено за день,
а также показывать затраты за отдельный месяц и за целый год.

В программе должно быть три endpoints:

/add/<date>/<int:number> — сохранение информации о совершённой 
в рублях трате за какой-то день;
/calculate/<int:year> — получение суммарных трат за указанный год;
/calculate/<int:year>/<int:month> — получение суммарных трат за 
указанные год и месяц.

Дата для /add/ передаётся в формате YYYYMMDD, 
где YYYY — год, MM — месяц (от 1 до 12), DD — число (от 01 до 31).
Гарантируется, что переданная дата имеет такой формат 
и она корректна (никаких 31 февраля).
"""


from datetime import datetime
from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    """
    сохранение информации о совершённой 
    в рублях трате за какой-то день

    Args:
        date (str): дата в формате YYYYMMDD.
        number (int): сумма в рублях.
    """
    try:
        its_date = datetime.strptime(date, '%Y%m%d')
        storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
        storage[year][month][day] += number

        storage[year][month].setdefault('month_total', 0) 
        storage[year].setdefault('year_total', 0)

        storage[year][month]['month_total'] += number
        storage[year]['year_total'] += number


        print(storage)

        return f"{year} {month} {day} траты: {number}"
    except ValueError:
        return 'Введите корректную дату!'





@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    """ получение суммарных трат за указанный год.

    Args:
        year (int): год.
    """
    year_expenses = storage[year]['year_total']
    return f'затраты за год {year}: {year_expenses}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    """
    получение суммарных трат за указанные год и месяц.

    Args:
        year (int): год.
        month (int): месяц.
    """
    month_expenses = storage[year][month]['month_total']
    return f'затраты за год {year} месяц {month}: {month_expenses}'


if __name__ == "__main__":
    app.run(debug=True)
