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
    for tower_id in cell_tower_ids:
        if tower_id <= 0:
            return 'Invalid cell_tower_id value.', 400
        
    for prefix in phone_prefixes:
        if not prefix[:-1].isdigit() or prefix[-1]!= '*':
            return 'Invalid phone_prefix value.', 400
        if len(prefix) > 11:
            return 'Invalid phone_prefix value.', 400
    
    for protocol in protocols:
        if protocol not in ['2G', '3G', '4G']:
            return 'Invalid protocol value.', 400
        
    if signal_level is not None and (-100 > signal_level > 0):
        return 'Signal level should be between -100 and 0.', 400
    
    if date_from is not None and not validate_date(date_from):
        return 'It should be in YYYYMMDD format.', 400
    
    if date_to is not None and not validate_date(date_to):
        return 'It should be in YYYYMMDD format.', 400
    
    if date_from and date_to:
        if date_from > date_to:
            return 'date_to should be greater than date_from.', 400


    # Если все проверки пройдены, выполняем поиск
    return (
        f"Search for {cell_tower_ids} cell towers. Search criteria: "
        f"phone_prefixes={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}, "
        f"date_from={date_from}, "
        f"date_to={date_to}"
    )


if __name__ == '__main__':
    app.run(debug=True)
