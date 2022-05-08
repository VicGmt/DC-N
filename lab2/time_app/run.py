from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def time():
    now = datetime.now()
    ttime = now.strftime("%H:%M:%S")
    return ttime


app.run(host='0.0.0.0',
        port=8080,
        debug=True)