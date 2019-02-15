from flask import Flask, jsonify, request, session,render_template
from flask_cors import CORS
import time
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

@app.route('/',methods=['GET'])
def start():
    return render_template('index.html')

@app.route('/homepage',methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/registerpage',methods=['GET'])
def registerpage():
    return render_template('index.html')

@app.route('/mainpage',methods=['GET'])
def mainpage():
    return render_template('index.html')


@app.route('/home', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form
        if user['username'] == 'huangkang' and user['password'] == 'kanghuang':
            session['username'] = user['username']
            session['password'] = user['password']
            return jsonify({'login': True, 'name': session['username'], 'password': session['password'],
                            'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'})
        else:
            return jsonify({
                'login': False
            })
    elif request.method == 'GET':
        if 'username' in session:
            return jsonify({'login': True, 'name': session['username'], 'password': session['password'],
                            'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'})
        return jsonify({'login': False})
    else:
        print('Neither')


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    if 'username' in session:
        return jsonify({'logout': False})
    else:
        return jsonify({'logout': True})


@app.route('/loadimage', methods=['GET'])
def load_image():
    images = []
    # return jsonify({'images': images})

    for i in range(100):
        single = {
            'thumbnail': 'https://github.com/Combo819/myPhotoBlog/blob/master/images/waterfall/DSC_1579.jpg?raw=true',
            'afterUrl': 'https://github.com/Combo819/myPhotoBlog/blob/master/images/waterfall/DSC_3362.jpg?raw=true',
            'beforeUrl': 'https://github.com/Combo819/myPhotoBlog/blob/master/images/waterfall/DSC_3565.jpg?raw=true',
            'uploadTime': i
        }
        images.append(single)

    return jsonify({'images': images})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': True, 'message': 'File does not exit'})
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': True, 'message': 'File not selected'})
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'error': False, 'message': 'Image uploaded!'})


@app.route('/main', methods=['GET'])
def main():
    if 'username' in session:
        return jsonify({'login': True, 'name': session['username'], 'password': session['password'],
                        'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'})
    return jsonify({'login': False})


if __name__ == '__main__':
    app.run(debug=True)