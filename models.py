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
        

