from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from baldpanda_site.users.utils import send_reset_email
from baldpanda_site import app, db, bcrypt
from baldpanda_site.users.forms import RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm
from baldpanda_site.models import User

users = Blueprint('users', __name__)

@users.route('/registration', methods = ['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}.', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', form = form)

@users.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', form = form)

@users.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('main.home'))

@users.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login_page'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return(redirect(url_for('users.reset_password')))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated', 'success')
        return redirect(url_for('users.login_page'))
    return render_template('reset_token.html', title='Reset Password', form=form)
