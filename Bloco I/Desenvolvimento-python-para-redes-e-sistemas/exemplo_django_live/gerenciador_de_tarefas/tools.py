from datetime import datetime
from dateutil import tz


def timestamp_converter(st_time):
    time = datetime.fromtimestamp(st_time, tz=tz.tzlocal()).strftime('%d/%m/%Y-%H:%M')
    return time
