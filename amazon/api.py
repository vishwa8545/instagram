import os
from flask import request,jsonify,send_from_directory,render_template,session
from flask_bootstrap import Bootstrap
from amazon import app
from amazon.models import products,users
Bootstrap(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')


@app.route('/api/user',methods = ['post'])
def login():
    op_type = request.form['op_type']
    username= request.form['username']
    password = request.form['password']
    if op_type == 'insert':
        name = request.form['name']
        sucess = users.signup(name,username,password)
        if sucess:
            user = users.search_by_name(username)
            session['user_id'] = str(user['_id'])
            return render_template('home.html',name = name)
        else:
            return render_template('index.html',message = 'signup was not sucessfull')
    if op_type == 'login':
        sucess = users.athuonticate(username,password)

        if sucess:
            matched = users.search_by_name(username)
            session['user_id'] = str(matched['_id'])
            return render_template('home.html', name = matched['name'])
        else:
            return render_template('index.html',message ='incorrect username/password')


@app.route('/api/upload', methods =['GET','POST'])
def upload():
    post = request.form['post_data']
    user_id = session['user_id']
    posts =  users.add_post(post,user_id)


    if posts:
        return render_template('home.html',posts = posts)

    else:
        return render_template('post.html', message ="the post is not added")
