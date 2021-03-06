from sqlalchemy.orm import backref
from . import login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from . import db

@login_manager.user_loader
def load_user(user_id): 
  return User.query.get(int(user_id))

class User(UserMixin,db.Model): 
  __tablename__ = 'users'
  
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),index = True)
  email = db.Column(db.String(255),unique = True, index = True)
  pitcher = db.relationship('Pitcher',backref = 'user',lazy = "dynamic")
  pass_secure  = db.Column(db.String(255))

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

class Pitcher(db.Model):
    __tablename__ = 'pitchers'
    
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255),index = False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    
    