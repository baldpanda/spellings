from flask import Flask, render_template

app = Flask(__name__)
sample_sentence = ("The _ _ _ sat on the mat.")


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/spellings')
def spelling_page():
    return render_template('spellings.html', sample_sentence = sample_sentence)

if __name__ == '__main__':
    app.run(debug = True)
