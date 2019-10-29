from datetime import datetime
from datetime import time
from collections import OrderedDict

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564626000, 'start': 1564647600}
]

PERMANENT_FARE = 0.36
DAY_RATE = 0.09

get_ends = list(filter(None, map(lambda elem: 
    elem['end']
    if elem['end'] > elem['start']
    else records.remove(elem),
    records)))

get_starts = list(map(lambda elem: elem['start'], records))

hour_starts = list(map(lambda elem: datetime.fromtimestamp(elem).hour, get_starts))

duration_call_in_seconds = list(map(lambda elemEnd, elemStart:
    elemEnd - elemStart, get_ends, get_starts))

total_fare = list(map(lambda elemStart, elemDuration:
    round(PERMANENT_FARE + (DAY_RATE * (elemDuration/60)), 2)
    if (elemStart > 6 and elemStart < 22)
    else PERMANENT_FARE,
    hour_starts, duration_call_in_seconds))

def classify_by_phone_number(records):
    get_infos = {}

    for record in records:
        number = record.get('source', 0)
        get_infos[number] = (get_infos.get(number, 0.0) + total_fare[records.index(record)])
    
    get_infos = OrderedDict(sorted(get_infos.items(), key=lambda kv: kv[1], reverse=True))

    records_answer = []
    for number, total in get_infos.items():
        records_answer.append({'source': number, 'total': round(total, 2)})
        
    return records_answer
