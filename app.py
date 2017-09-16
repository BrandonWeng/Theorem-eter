from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Team Wave HTN GANG '


@app.route('/test_post', methods=['GET', 'POST'])
def test_post():
    if request.method == 'GET':
        return "GET"
    else:
        return "POST"
