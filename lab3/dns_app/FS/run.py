from flask import Flask, request, Response
import requests
import json


app = Flask(__name__)


@app.route('/')
def FS_route():
    return 'Welcome to FS'

# UDP to Server
@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '0.0.0.0'
    dict = {}
    dict['name'] = host_name
    dict['address'] = ip_address
    req = requests.put('http://0.0.0.0:53533', data = dict)
    return Response(req.text, status = 201)

@app.route('/fibonacci')
def fabonacci():
    x_fibo = int(request.args.get('number'))
    if type(x_fibo) != int:
        return Response("ERROR: please input a number.", status = 400)
    result = fib(x_fibo)
    return Response("the fibo for {0} is: {1}".format(x_fibo, result), status = 200)



def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# app – running on port 9090

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
