# models.py
import flask_sqlalchemy
from app import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))
    
    def __init__(self, a):
        self.message = a

        
    def __repr__(self):
        return '<message: %s>' % self.message
        

class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(1000), unique=True)
    user = db.Column(db.String(1000), unique=True)
    pic = db.Column(db.String(1000), unique=True)
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'))
    
    def __init__(self, a, b, c, d):
        self.email = a
        self.user = b
        self.pic = c
        self.message_id = d

        
    def __repr__(self):
        return {
            '<email: %s>' % self.email,
            '<user: %s>' % self.user,
            '<pic: %s>' % self.pic,
            '<message_id: %s>' & self.message_id
            }