from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    tasks = db.relationship('Tasks')


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50000))
    data_title = db.Column(db.String(10000))
    due_date = db.Column(db.String(11))
    completed = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
