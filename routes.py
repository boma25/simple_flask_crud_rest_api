from app import app
from serializers import UsersSchema
from flask import jsonify, request
from db import db
from model import Users
import bcrypt


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


# login or create route
@app.route('/sign_up', methods=['Post'])
def signUp():
    username = request.json['username']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    age = request.json['age']

    if Users.query.filter_by(username=username).all():
        return 'a user with this username already exist'

    password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = Users(username=username, password=password,
                     first_name=first_name, last_name=last_name, age=age)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# get all users
@app.route('/users')
def getUsers():
    users_list = Users.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


# get a single user
@app.route('/user/<int:id>')
def getuser(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify(result)
    return 'user does not exist'


# login route
@app.route('/login', methods=['Post'])
def login():
    username = request.json['username']
    password = request.json['password']
    user = Users.query.filter_by(username=username).first()

    if user == None:
        return 'user does not exist'
    if bcrypt.checkpw(password.encode('utf-8'), user.password):
        return 'login successfull'
    else:
        return "incorrect password"


# update route
@app.route('/update/<int:id>', methods=['Put'])
def update(id):
    age = request.json['age']
    user = Users.query.get(id)
    if user == None:
        return 'user does not exist'

    user.age = age
    db.session.commit()

    return user_schema.jsonify(user)


# delete route
@app.route('/delete/<int:id>', methods=['Delete'])
def delete(id):
    user = Users.query.get(id)
    if user == None:
        return 'user does not exist'
    db.session.delete(user)
    db.session.commit()
    return f'{user.username} has been deleted successfully'
