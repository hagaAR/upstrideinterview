from flask import Flask
from flask import request
import requests
app = Flask(__name__)

backend_url = 'http://127.0.0.1:5000/pipeline'

@app.route('/pipeline/put', methods=['PUT'])
def run_pipeline():
    json_data = {'pipeline':'start'}
    res = requests.put(backend_url, json=json_data)
    return res.content

@app.route('/pipeline/get', methods=['GET'])
def status_pipeline():
    return requests.get(backend_url).content