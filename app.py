import os
from flask import Flask, request,flash, jsonify, send_from_directory, abort
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
    return 'Team Wave HTN 2017 robot.txt??'


@app.route('/test_post', methods=['GET', 'POST'])
def test_post():
    return request.method


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():

    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "FAILED no file found"

        file = request.files['file']
        filename = secure_filename(file.filename)

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "FAILED : file name is empty"

        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #TODO : result will be determined based on the list of keywords hanyu/mike provides
            result = {
                'basis': 'uWaterlooMath136_1,uWaterlooMath136_2',
                'angular': 'uWaterlooMath136_3,uWaterlooMath136_4'
            }

            return jsonify({'upload': True, 'name': filename, 'result': result})

    return jsonify({'upload': False})


@app.route('/get/picture/<string:name>', methods=['GET'])
def send_pics(name):
    pics = open("img/" + name)
    if pics:
        return send_from_directory(app.config['UPLOAD_FOLDER'], name)

    abort(404)


if __name__ == "__main__":
    app.run()