from flask import Flask
import os



app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


app.run(host='0.0.0.0', port=81, debug=True)
