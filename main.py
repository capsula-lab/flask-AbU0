import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/api/<name>/<email>')
def create_task(name, email):
    f = open("guests.txt", "a")
    f.write("Name:")
    f.write(name)
    f.write("Email:")
    f.write(email)
    f.write("|||")
    f.close()
    return "alles gut"

@app.route('/add/')
def createcm():
   summary  = request.args.get('summary', None)
   change  = request.args.get('change', None)

@app.route('/api/get/getTheGuests')
def get_guests():
    f = open("guests.txt", "r")
    guests = f.read()
    f.close()
    return jsonify(guests)


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


