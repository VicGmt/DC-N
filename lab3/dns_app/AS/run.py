# AS

# Imports

from flask import Flask
from flask import request
from flask import Response
from time import gmtime, strftime
import json
import os

app = Flask(__name__)


@app.route('/home')
def AS_route():
    return "AS HOME"


@app.route('/', methods=['GET', 'PUT'])
def AS():

    #setting up the file:

    file = 'rcrd_dns.json'
    if not os.path.exists(file):
        os.system(r'touch rcrd_dns.json')
        file = 'rcrd_dns.json'

    # loading the data into rcrd_dns

    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if key not in data:
                return Response("ERROR: hostname not found", status=404)
            else:
                address = data.get(key)
                return Response(address, status=200)

    else:
        data_get = request.form
        host_name = data_get['name']
        ip_address = data_get['address']
        dict = {}
        dict[host_name] = ip_address
        with open(file, 'w') as json_file:
            json.dump(dict, json_file)
        return Response("registered!", status=200)


# App running on port 5353

app.run(host='0.0.0.0',
        port=53533,
        debug=True)