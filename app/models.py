from sqlalchemy.orm import backref

from . import db

class User(db.Model): 
  __tablename__ = 'users'
  
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True, index = True)
 
 
  password_secure = db.Column(db.String(255))

class Pitcher(db.model):
    __tablename__ = 'pitchers'
    
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255),index = False)
    