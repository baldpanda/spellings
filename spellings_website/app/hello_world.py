#hello_word.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Bald Panda!</h1>'

@app.route('/spellings')
def spelling_page():
    return 'Placeholder for spellings'

if __name__ == '__main__':
    app.run(debug = True)
