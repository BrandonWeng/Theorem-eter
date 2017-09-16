import os
from flask import Flask, request, redirect, url_for,flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'img/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config["SECRET_KEY"] = "team wave HTN"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'

app.debug = True
@app.route('/')
def home():
    return 'Team Wave HTN 2017'


@app.route('/test_post', methods=['GET', 'POST'])
def test_post():
    return request.method


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':

        file = request.files['file']

        if file and allowed_file(file.filename):
            print("SAVING FILE")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "Success!"
        else:
            print(request.form)

    return 'Failed'


if __name__ == "__main__":
    app.run()