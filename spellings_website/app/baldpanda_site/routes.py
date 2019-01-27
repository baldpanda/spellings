from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from baldpanda_site import app, db, bcrypt, mail
from baldpanda_site.forms import (RegistrationForm, LoginForm, NewSentence, WordsForSheet,
                                    RequestResetForm, ResetPasswordForm)
from baldpanda_site.models import User, Sentence
from baldpanda_site.six_words_with_spaces import Six_words_with_blanks
from baldpanda_site.example_sentence import Example_sentence
from flask_mail import Message

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
        words_for_search = words_for_search.replace(" ", "")
        words_for_search = words_for_search.replace(",", "+")
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

@app.route('/sentence/<string:words_to_add>', methods = ['GET', 'POST'])
@login_required
def sentence_adder(words_to_add):
    form = NewSentence()
    if form.validate_on_submit():
        sentence_to_add_to_db = Example_sentence(form.sentence.data)
        sentence = " " + sentence_to_add_to_db.add_space_before_and_after_punct([",", ".", "!", "?", '"'])
        sentence = Sentence(sentence = sentence, user_id = current_user.id)
        db.session.add(sentence)
        db.session.commit()
        flash('Your sentence has been added', 'success')
        return(redirect(url_for('spelling_page')))
    return render_template('sentence_adder_page.html', title = 'sentence_adder',
    form = form, words_to_add = words_to_add)

@app.route('/worksheet/<string:words>')
def word_search(words):
    sentence_list = [[],[]]
    words_list = words.split('+')
    words_for_page = words.replace('+', ', ')
    words_not_in_db = ''
    for word in words_list:
        six_words = Six_words_with_blanks()
        sentence_list[0].append(six_words.generate_six_words_with_blanks(word))
        string_to_query_in_middle = f"% {word} %"
        sentence = Sentence.query.filter(Sentence.sentence.like(string_to_query_in_middle)).first()
        if sentence:
            sentence_with_blanks = Example_sentence(sentence.sentence)
            sentence_with_blanks.sentence = sentence_with_blanks.remove_space_before_and_after_punct(
            [",",".", "!", "?",'"'])
            sentence_list[1].append(sentence_with_blanks.blank_out_word_in_sentence(word))
        else:
            words_not_in_db += word + "+"
    if len(words_not_in_db) == 0:
        return render_template('worksheet.html', sample_sentences = sentence_list, words = words_for_page)
    else:
        words_not_in_db = words_not_in_db[:-1]
        return redirect(url_for('sentence_adder', words_to_add=words_not_in_db))

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='baldpanda94@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password visit the following link:
    {url_for('reset_token', token=token, _external=True)}

    If you did not request this email, please ignore.
    '''
    mail.send(msg)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('login_page'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return(redirect(url_for('reset_password')))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated', 'success')
        return redirect(url_for('login_page'))
    return render_template('reset_token.html', title='Reset Password', form=form)
