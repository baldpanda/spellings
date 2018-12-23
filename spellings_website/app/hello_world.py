from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b15f64dade99ceb17ee15983fa4bc80'
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

@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', sample_sentence = sample_sentence,form = form)

if __name__ == '__main__':
    app.run(debug = True)
