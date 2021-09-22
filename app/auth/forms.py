from enum import unique

from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from werkzeug.utils import redirect
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired, Required,Email,Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)]) 
    remember = BooleanField('remember me')
class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Length( max=15)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])     
