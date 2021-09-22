from flask import Flask, render_template,redirect,url_for
from .forms import LoginForm,RegisterForm
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    
        
    return render_template('login.html', form=form)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
   
        
    return render_template('signup.html', form=form)