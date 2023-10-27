from app import app
from app.controller import UserController


@app.route('/users')
def users():
    return UserController.index()


@app.route('/users/<id>')
def usersDetail(id):
    print(id)
    return UserController.show(id)
