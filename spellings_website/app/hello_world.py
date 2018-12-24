from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b15f64dade99ceb17ee15983fa4bc80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

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

if __name__ == '__main__':
    app.run(debug = True)
