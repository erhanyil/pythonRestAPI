from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = SQLAlchemy(app)


class studentModel(db.Model):
    __tablename__ = 'students'
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    student = []

'''
def __init__(self, name, city, addr, pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

'''

def __init__(self, student):
    self.name = student['name']
    self.city = student['city']
    self.addr = student['addr']
    self.pin = student['pin']


db.create_all()
