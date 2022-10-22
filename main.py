from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_url_path='', static_folder='frontend/build')

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
