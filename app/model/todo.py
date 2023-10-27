from app import db
from datetime import datetime
from .user import Users


class Todos(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    users = db.relationship('Users', backref='user_id')

    def __repr__(self):
        return '<Todo {}>'.format(self.todo)
