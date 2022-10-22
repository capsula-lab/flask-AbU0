from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory('frontend/build/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
