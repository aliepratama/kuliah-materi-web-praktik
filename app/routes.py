from app import app
from app.controller import UserController
from flask import request


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()


@app.route('/users/<id>')
def usersDetail(id):
    return UserController.show(id)
