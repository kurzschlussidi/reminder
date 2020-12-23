from datetime import datetime
from flask import Flask, request, redirect, url_for
from flask import render_template
import math


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def editor():
    if request.method == "POST":
        url = request.url
        sender = request.form["sender"]
        receiver = request.form["receiver"]
        date = request.form["date"]
        if not sender or not receiver or not date:
            return render_template('editor.html',link = None, error = True)
        try:
            datetime.strptime(date, '%Y-%m-%d-%H-%M')
        except:
            return render_template('editor.html',link = None, error = True)

        link = url + "r?sender=" + sender + "&receiver=" + receiver + "&date=" + date
        return render_template('editor.html',link = link)
    else:
        return render_template('editor.html',link = None)

@app.route("/r")
def reminder():
    print("responding")
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    send_date = request.args.get('date')
    if not sender or not receiver or not send_date:
        return redirect(url_for("editor"))
    try:
        time_send = datetime.strptime(send_date, '%Y-%m-%d-%H-%M')
    except:
        return redirect(url_for("editor"))
    duration = datetime.now()-time_send
    days = duration.days
    hours = math.floor(duration.seconds/3600)
    minutes = math.floor((duration.seconds % 3600)/60)
    return render_template('main.html', sender=sender, receiver=receiver, duration_d=days, duration_h=hours, duration_m=minutes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("8000"), debug=False)