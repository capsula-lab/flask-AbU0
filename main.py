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

@app.route('/add')
def createcm():
   name  = request.args.get('name', None)
   email  = request.args.get('email', None)
   values_list = gsheet.col_values(1)
   target = len(values_list) + 1;
   gsheet.update_cell(target, 1, name)
   gsheet.update_cell(target, 2, email)
   return render_template("index.html")



if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


