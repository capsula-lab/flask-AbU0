import os
from flask import Flask, render_template, jsonify

app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/api/<name>')
def create_task(name):
    f = open("guests.txt", "a")
    f.write(name)
    f.close()
    return "alles gut"

@app.route('/api/get/getTheGuests')
def create_task(name):
    f = open("guests.txt", "r")
    guests = f.read()
    f.close()
    return jsonify(guests)


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


