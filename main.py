import os
from flask import Flask, jsonify, render_template, request, abort
# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')


credential = ServiceAccountCredentials.from_json_keyfile_name("secrets.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("RSVP").sheet1

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/getSheet', methods=["GET"])
def getSheet():
    values_list = gsheet.col_values(1)
    length = values_list.length();
    return jsonify(length)

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

@app.route('/add')
def createcm():
   name  = request.args.get('name', None)
   email  = request.args.get('email', None)
   f = open("guests.txt", "a")
   f.write("Name:")
   f.write(name)
   f.write("Email:")
   f.write(email)
   f.write("|||")
   f.close()
   return "alles gut2"

@app.route('/api/get/getTheGuests')
def get_guests():
    f = open("guests.txt", "r")
    guests = f.read()
    f.close()
    return jsonify(guests)


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


