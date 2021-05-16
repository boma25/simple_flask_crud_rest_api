from db import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.username
