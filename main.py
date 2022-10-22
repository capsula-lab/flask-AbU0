import os
from flask import Flask, render_template
import psycopg2

app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)




#connect to the db
con = psycopg2.connect(
    host = "containers-us-west-50.railway.app",
    database = "railway",
    user = "postgres",
    password = "Yqew4AGn38m9TpdNHzsW",
    port = "7453"
)
app = Flask(__name__, static_url_path='',
                  static_folder='react',
                  template_folder='react')

cur = con.cursor()

cur.execute("SELECT * FROM attendees")

#close connection to the db
con.close()