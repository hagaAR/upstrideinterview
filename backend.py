import time
from flask import Flask, session, request
from flask_session import Session
app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/pipeline', methods=['PUT'])
def run_pipeline():
    json_data = request.json
    if json_data['pipeline'] == 'start':
        session['key'] = 'starting'
        time.sleep(10)
        session['key'] = 'started'
        return {'pipeline':'started'}
    return status_pipeline()

@app.route('/pipeline', methods=['GET'])
def status_pipeline():
    return {'pipeline': session.get('key')}

@app.route('/pipeline/reset', methods=['PUT'])
def reset_pipeline():
    json_data = request.json
    if json_data['pipeline'] == 'reset':
        session['key'] = ''
    return status_pipeline()