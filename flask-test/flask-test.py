from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
	return 'Server is online.';

@app.route('/shutdown', methods=['GET'])
def shutdown():
	shutdown_server()
	return 'Server is shutting down.'

@app.route('/postData', methods=['POST'])
def postData():
    data = request.json
	res = jsonify(data)
	return res

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app.run(port=80)
