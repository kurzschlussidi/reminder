from datetime import datetime
from flask import Flask, request
from flask import render_template
import math


app = Flask(__name__)

@app.route("/")
def index():
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    send_date = request.args.get('date')
    if not sender or not receiver or not send_date:
        url = request.url_root
        return render_template('tutorial.html',url=url)
    try:
        time_send = datetime.strptime(send_date, '%Y-%m-%d-%H-%M')
    except:
        url = request.url_root
        return render_template('tutorial.html', url=url)
    duration = datetime.now()-time_send
    days = duration.days
    hours = math.floor(duration.seconds/3600)
    minutes = math.floor((duration.seconds % 3600)/60)
    return render_template('main.html', sender=sender, receiver=receiver, duration_d=days, duration_h=hours, duration_m=minutes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8000"), debug=False)