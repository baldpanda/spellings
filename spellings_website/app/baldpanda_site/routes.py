from flask import render_template, url_for, flash, redirect
from baldpanda_site import app, db, bcrypt
from baldpanda_site.forms import RegistrationForm, LoginForm
from baldpanda_site.models import User

sample_sentence = ("The _ _ _ sat on the mat.")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spellings')
def spelling_page():
    return render_template('spellings.html', sample_sentence = sample_sentence)

@app.route('/registration', methods = ['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', sample_sentence = sample_sentence, form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'pcallery@baldpanda.com' and form.password.data == 'password':
            flash('Successful Login', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', sample_sentence = sample_sentence,form = form)
