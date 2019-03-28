"""Forms for adding sentences to db and
submitting required words to worksheet
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NewSentence(FlaskForm):
    """Form for adding new sentence to db"""
    sentence = StringField('Please enter a sentence you would like to add.', validators=[DataRequired()])
    submit = SubmitField('Submit')

class WordsForSheet(FlaskForm):
    """Form for submitting required words for worksheet"""
    words = StringField("Please enter the spellings for the worksheet,\
     separating them using a comma.", validators=[DataRequired()])
    submit = SubmitField('Make Worksheet')

class SentenceToDelete(FlaskForm):
    """Form for finding sentence user would like to delete"""
    sentence = StringField('Please enter part of sentence you would like to delete.'\
    , validators=[DataRequired()])
    submit = SubmitField('Find Sentence To Delete')

class DeleteSentence(FlaskForm):
    """Form for deleting a sentence"""
    sentence = StringField('Would you like to delete the following sentence?'\
    , validators=[DataRequired()])
    submit = SubmitField('Delete Sentence')
