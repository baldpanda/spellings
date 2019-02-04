from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NewSentence(FlaskForm):
    sentence = StringField('Sentence', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WordsForSheet(FlaskForm):
    words = StringField('Please enter the required words, seperating them using a comma.'
    , validators=[DataRequired()])
    submit = SubmitField('Make Worksheet')
