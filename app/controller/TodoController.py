from app.model.todo import Todos as Todo
from flask import request, jsonify
from app import response, db
from app.controller import UserController
from flask_jwt_extended import *


@jwt_required()
def index():
    try:
        id = request.args.get('user_id')
        todo = Todo.query.filter_by(user_id=id).all()
        data = transform(todo)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def store():
    try:
        todo = request.json['todo']
        dec = request.json['description']
        user_id = request.json['user_id']

        todo = Todo(todo=todo, description=dec, user_id=user_id)
        db.session.add(todo)
        db.session.commit()

        return response.ok('', 'Successfully create todo!')
    except Exception as e:
        print(e)


def update(id):
    try:
        todo = request.json['todo']
        desc = request.json['description']

        todo = Todo.query.filter_by(id=id).first()
        todo.todo = todo
        todo.description = desc

        db.session.commit()

        return response.ok('', 'Successfully update todo!')
    except Exception as e:
        print(e)


def show(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], 'Empty ...')

        data = singleTransform(todo)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def delete(id):
    try:
        todo = Todo.query.filter_by(id=id).first()
        if not todo:
            return response.badRequest([], 'Empty ...')
        db.session.delete(todo)
        db.session.commit()

        return response.ok('', 'Successfully delete todo!')
    except Exception as e:
        print(e)


def transform(values):
    array = []
    for i in values:
        array.append(singleTransform(i))
    return array


def singleTransform(values):
    data = {
        'id': values.id,
        'user_id': values.user_id,
        'todo': values.todo,
        'description': values.description,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
        'user': UserController.singleTransform(values.users, withTodo=False)
    }
    return data


@jwt_required(refresh=True)
def refresh():
    try:
        user = get_jwt_identity()
        new_token = create_access_token(identity=user)

        return response.ok({
            'token_access': new_token
        }, "")
    except Exception as e:
        print(e)
