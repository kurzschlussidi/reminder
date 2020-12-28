from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template
from random import randint
import math
import sqlite3
import os 
import string
import random


dir_path = os.path.dirname(os.path.realpath(__file__))

database_location = dir_path + "/data/database.db"
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

        key = setData(sender, receiver, date)
        link = url + str(key)
        return render_template('editor.html',link = link)
    else:
        return render_template('editor.html',link = None)

@app.route("/<key>")
def reminder(key):
    if not isKey(key):
        return redirect(url_for("editor"))
    (sender, receiver, date) = getData(key)
    time_send = datetime.strptime(date, '%Y-%m-%d-%H-%M')
    duration = datetime.now()-time_send
    days = duration.days
    hours = math.floor(duration.seconds/3600)
    minutes = math.floor((duration.seconds % 3600)/60)
    return render_template('main.html', sender=sender, receiver=receiver, duration_d=days, duration_h=hours, duration_m=minutes)

def checkTable():
    conn = sqlite3.connect(database_location)
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='main' ''')
    if c.fetchone()[0]==1 :
        conn.close()
        return True
    else:
        conn.close()
        return False
    

def makeTable():
    conn = sqlite3.connect(database_location)
    c = conn.cursor()
    c.execute("""CREATE TABLE main (
                key text,
                sender text,
                receiver text,
                date text
                )""")
    conn.commit()
    conn.close()
    return

def setData(sender, receiver, date):
    conn = sqlite3.connect(database_location)
    c = conn.cursor()
    key = genKey()
    while isKey(key):
        key = genKey()
    c.execute("INSERT INTO main VALUES (?, ?, ?, ?)",(key, sender, receiver, date))
    conn.commit()
    conn.close()
    return key

def getData(key):
    conn = sqlite3.connect(database_location)
    c = conn.cursor()
    c.execute("SELECT * FROM main WHERE key=?", (key, ))
    (key, sender, receiver, date)= c.fetchone()
    return (sender, receiver, date)

def isKey(key):
    conn = sqlite3.connect(database_location)
    c = conn.cursor()
    c.execute("SELECT * FROM main WHERE key=?", (key, ))
    if c.fetchone() == None:
        conn.close()
        return False
    else:
        conn.close()
        return True
    
def genKey():
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(6))

if __name__ == '__main__':
    if not checkTable():
        makeTable()
    app.run(host="0.0.0.0", port=int("8000"), debug=False)