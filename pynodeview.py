from flask import Flask
from flask import render_template, jsonify, request
import json
import numpy as np
import string, random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_json_data():
    with open('templates/myjson.json') as json_data:
        d = json.load(json_data)
    return jsonify(d)


if __name__ == '__main__':
    app.run()
    app.debug = True
    #app.run(port=5000)

