from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Team Wave HTN 2017'


@app.route('/test_post', methods=['GET', 'POST'])
def test_post():
    if request.method == 'GET':
        return "GET"
    else:
        return "POST"

