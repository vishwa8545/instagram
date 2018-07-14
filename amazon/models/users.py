import  os
from flask import send_from_directory,render_template,session
from amazon.models import users
from bson import ObjectId
from amazon.models import db



def search_by_id(user_id):
    user = {
        '_id':ObjectId(user_id)
    }

    matches = db['users'].find(user)
    if matches.count()>0:
        return matches[0]['posts']
    else :
        return None

def search_by_name(name):
    user = {
        'username':name
    }

    matches = db['users'].find(user)
    if matches.count()>0:
        return matches.next()
    else :
        return None

def signup(name,username,password):
    existing_user = search_by_name(username)
    if existing_user is not None:
        return False
    else:
        user = {
        'name': name,
        'username': username,
        'password': password
        }
        db['users'].insert_one(user)
        return True
def athuonticate(username,password):

    user = search_by_name(username)
    if user is None:
        return False

    if user['password'] == password:
        return True
    else:
        return False
def add_post(post_text,user_id):
    posts ={
        'user_id':ObjectId(user_id),
        'post_data':post_text
    }
    db['posts'].insert_one(posts)
    filter = {
        'user_id':ObjectId(user_id)
    }
    cursor = db['posts'].find(filter)
    if cursor.count()>0:
        return cursor
    else:
        return False
def search_by_post_name(post_text):
    filter = { 'post_data':post_text}
    cursor = db['posts'].find(filter)
    print(type(cursor))
    if cursor.count()>0:
        return cursor[0]['_id']
    else:
        return None