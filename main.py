import os
from flask import Flask, jsonify, render_template, request, abort
# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')

def create_keyfile_dict():
    variables_keys = {
  "type": os.environ['type'],
  "project_id": os.environ["project_id"],
  "private_key_id": os.environ["private_key_id"],
  "private_key": os.environ["private_key"],
  "client_email": os.environ[ "client_email"],
  "client_id": "client_id",
  "auth_uri": os.environ["auth_uri"],
  "token_uri": os.environ["token_uri"],
  "auth_provider_x509_cert_url": os.environ[ "auth_provider_x509_cert_url"],
  "client_x509_cert_url": os.environ["client_x509_cert_url"]
}
    return variables_keys
@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/add')
def createcm():
   name  = request.args.get('name', None)
   email  = request.args.get('email', None)
   credential = ServiceAccountCredentials.from_json_keyfile_dict(create_keyfile_dict(), ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
   client = gspread.authorize(credential)
   gsheet = client.open("RSVP").sheet1
   values_list = gsheet.col_values(1)
   target = len(values_list) + 1;
   gsheet.update_cell(target, 1, name)
   gsheet.update_cell(target, 2, email)
   return render_template("index.html")



if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)


