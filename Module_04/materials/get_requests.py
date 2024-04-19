from datetime import datetime
from flask import Flask, request
from typing import List, Optional


app = Flask(__name__)


def validate_date(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, '%Y%m%d')
        return True
    except ValueError:
        return False


# /search/3/12/2/1/1/999*/2/2G/4G/1/-100
@app.route(
    "/search/", methods=["GET"],
)
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)

    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    protocols: List[str] = request.args.getlist("protocol")
    signal_level: Optional[float] = request.args.get(
        "signal_level", type=float, default=None
    )
    date_from: Optional[str] = request.args.get('date_from')
    date_to: Optional[str] = request.args.get('date_to')

    # проверка параметров:
    

    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
    )


if __name__ == '__main__':
    app.run(debug=True)
