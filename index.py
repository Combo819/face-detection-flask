from flask import Flask, jsonify, request, session,render_template
from flask_cors import CORS
import time
import os
from werkzeug.utils import secure_filename
import mysql.connector



app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

cnx = mysql.connector.connect(user='root',password='mysql8013',host='127.0.0.1',database='test',auth_plugin='mysql_native_password')
cursor=cnx.cursor()

UPLOAD_FOLDER = './images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

posts = [
{ 'title':"as we can",'content':"my name is van. I am an artist, a performance artist",'owner':"billy herrington",'email':'123@qq.com','image':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'openClose':True,'avatar':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'postId':"123456",'wantRent':True},
{ 'title':"as we cannot",'content':"my name is van. I am an artist, a performance artist",'owner':"billy herrington",'email':'123@qq.com','image':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'openClose':False,'avatar':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'postId':"1234567",'wantRent':True},
{ 'title':"as we can do",'content':"my name is van. I am an artist, a performance artist",'owner':"billy herrington",'email':'123@qq.com','image':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'openClose':True,'avatar':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'postId':"1234568",'wantRent':False},
{ 'title':"i am an artist",'content':"my name is van. I am an artist, a performance artist",'owner':"billy herrington",'email':'123@qq.com','image':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'openClose':True,'avatar':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",'postId':"123456",'wantRent':False}
]

post_detail={
    'title':"as we can",
  'content':"my name is van. I am an artist, a performance artist",
  'owner':"billy herrington",
  'images':["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
           ],
  'openClose':False,
  'avatar':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd3RWAZiYjGHj4Hv_RjtpqL64lpHs4-qaLshz0Er7IpeV8S4qdrw",
  'postId':"123456",
  'wantRent':True,
  'email': '123@qq.com',
    'comments':[
        {'user':'billy herrington','avatar':'https://vignette.wikia.nocookie.net/unanything/images/e/e1/Billy.jpg/revision/latest?cb=20160817140541','content':'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.'}
    ,   {'user':'Ricardo Milos','avatar':'https://pbs.twimg.com/media/Dxcrkq9XcAIAFxW.jpg','content':'I may be late but never absent'}

    ]
  }

@app.route('/signin',methods=['POST'])
def signin():
    user = request.form
    print(user['email'])
    if user['email'] == '1' and user['password'] == '1':
        session['username'] = 'van dark'
        print(session)
        #session['email'] == user['email']
        session['password'] = user['password']
        return jsonify({'login': True, 'name': session['username'],
                        'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'})
    else:
        return jsonify({
            'login': False
        })

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    if 'username' in session:
        return jsonify({'logout': False})
    else:
        return jsonify({'logout': True})

@app.route('/get_all_list',methods=['GET'])
def get_all_list():
    return jsonify({'status':True,'posts':posts})


@app.route('/get_detail',methods=['GET'])
def get_detail():
    postId = request.args.get('postId')
    print('postId:{}'.format(postId))
    return jsonify({'status':True,'detail':post_detail})

@app.route('/get_profile',methods=['GET'])
def get_profile():
    owner = request.args.get('owner')
    print(owner)
    return jsonify({
        'owner':'van darkholme',
        'email':'1234567@mail.utoronto.ca',
        'avatar':'https://ch.mathworks.com/matlabcentral/profiles/12606575_1529306722027.jpg',
        'postList':[{'postId':"1234567",'title':'change my whole entire house into a '},
                    {'postId': "1234568", 'title': 'and it go on very well'},
                    ]
    })

@app.route('/check_signin',methods=['GET'])
def check_signin():
    if 'username' in session:
        return jsonify({'signin': True, 'name': session['username'],
                        'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'})
    else:
        return jsonify({'signin':False})


@app.route('/delete_photo',methods=['POST'])
def delete_photo():
    image = request.form
    print(image['remove'])
    return jsonify({'delete':True,'image':image['remove']})


@app.route('/edit_submit',methods=['post'])
def edit_submit():
    submit = request.form
    print(submit)
    return jsonify({
        'submit':True
    })
'''
form.append('title',this.state.title)
form.append('content',this.state.content)
form.append('type',this.state.type)
form.append('status',this.state.status)
form.append('postId',store.getState().edit)  if postId=='',it's a new post
'''

@app.route('/signup_new',methods=['POST'])
def signup_new():
    session['username'] = request.form['username']
    return jsonify({
        'status':True,
        'name':session['username'],
        'avaSrc': 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'
    })



if __name__ == '__main__':
    app.run(debug=True)