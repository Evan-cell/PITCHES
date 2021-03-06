from flask import render_template,redirect,url_for,request,flash
from .forms import LoginForm,RegisterForm
from flask_login import login_user,logout_user,login_required
from . import auth
from .. import db
from ..models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data): 
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.pitches'))
    
        flash('Invalid username or Password')
    
    
        
    return render_template('login.html', form=form)
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit(): 
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
   
        
    return render_template('signup.html', form=form)