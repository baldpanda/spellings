"""Forms for adding sentences to db and
submitting required words to worksheet
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NewSentence(FlaskForm):
    """Form for adding new sentence to db"""
    sentence = StringField('Sentence', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WordsForSheet(FlaskForm):
    """Form for submitting required words for worksheet"""
    words = StringField('Please enter the required words, seperating them using a comma.'\
    , validators=[DataRequired()])
    submit = SubmitField('Make Worksheet')
