from app import app
from app.controller import UserController


@app.route('/users')
def users():
    return UserController.index()
