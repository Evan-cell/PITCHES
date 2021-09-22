from enum import unique
from flask import Flask, render_template,redirect,url_for
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from werkzeug.utils import redirect
from wtforms import StringField,PasswordField,BooleanField
from wtforms.validators import InputRequired, Required,Email,Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

Bootstrap(app)



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)]) 
    remember = BooleanField('remember me')
class RegisterForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(), Length( max=15)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])     

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    
        
    return render_template('login.html', form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
   
        
    return render_template('signup.html', form=form)

@app.route('/pitches')
def dashboard():
    return render_template('pitches.html')

if __name__ == '__main__':
    app.run(debug=True)