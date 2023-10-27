from app.model.user import Users
from app import response, app, db
from flask import request


def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email,
        })
    return array


def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data


def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty ...')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.ok('', 'Successfully create data!')
    except Exception as e:
        print(e)
