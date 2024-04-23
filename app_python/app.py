from datetime import datetime

import pytz
from flask import Flask

app = Flask(__name__)

VOLUME="volume/visits.txt"

@app.route("/")
def show_moscow_time():

    # constant for timezone
    TIMEZONE = "Europe/Moscow"

    # get time and its fields
    time = datetime.now(tz=pytz.timezone(TIMEZONE))
    hours = time.hour
    minutes = time.minute
    seconds = time.second

    # construct result HTML soup and return it
    time_string = f"{hours}:{minutes}:{seconds}"
    html = f"<center style='font-size: 60px;'>{time_string}</center>"
    with open(VOLUME, 'a') as f:
        f.write(time_string)
        f.write('\n')
    return html

@app.route("/visits")
def visits():
    with open(VOLUME, 'r') as f:
        visits = f.readlines()
    return '\n'.join(visits)
