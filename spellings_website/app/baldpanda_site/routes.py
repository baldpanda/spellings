from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from baldpanda_site import app, db, bcrypt
from baldpanda_site.forms import RegistrationForm, LoginForm, NewSentence, WordsForSheet
from baldpanda_site.models import User, Sentence

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/worksheet', methods = ['GET', 'POST'])
def spelling_page():
    form = WordsForSheet()
    sentence_list = []
    if form.validate_on_submit():
        words_for_search = form.words.data
        return redirect(url_for('word_search', words = words_for_search))
    return render_template('wordsearch.html', sample_sentences = sentence_list, form = form)

@app.route('/registration', methods = ['GET', 'POST'])
def registration_page():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created successfully for {form.username.data}.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('home'))

@app.route('/sentence/new', methods = ['GET', 'POST'])
@login_required
def sentence_adder():
    form = NewSentence()
    if form.validate_on_submit():
        sentence = Sentence(sentence = form.sentence.data, user_id = current_user.id)
        db.session.add(sentence)
        db.session.commit()
        flash('Your sentence has been added', 'success')
        return(redirect(url_for('home')))
    return render_template('sentence_adder.html', title = 'sentence_adder', form = form)

@app.route('/worksheet/<string:words>')
@login_required
def word_search(words):
    sentence_list = []
    words_list = words.split('+')
    for word in words_list:
        string_to_query_in_middle = f"% {word} %"
        string_to_query_at_front = f"{word} %"
        string_to_query_at_end = f"% {word}."
        sentence = Sentence.query.filter(Sentence.sentence.like(string_to_query_in_middle)
        | Sentence.sentence.like(string_to_query_at_front)
        | Sentence.sentence.like(string_to_query_at_end)).first().sentence
        sentence_list.append(sentence)
    return render_template('spellings.html', sample_sentences = sentence_list)
