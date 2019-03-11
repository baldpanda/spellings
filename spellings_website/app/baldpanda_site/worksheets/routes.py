"""Routes associated with spelling worksheets"""
from flask import render_template, url_for, redirect, Blueprint, flash
from flask_login import login_required, current_user
from baldpanda_site import db
from baldpanda_site.worksheets.sentences.example_sentence import ExampleSentence
from baldpanda_site.worksheets.forms import  WordsForSheet, NewSentence
from baldpanda_site.models import Sentence
from baldpanda_site.worksheets.blanked_words.six_words_with_spaces import SixWordsWithBlanks

worksheets = Blueprint('worksheets', __name__)

@worksheets.route('/worksheet', methods=['GET', 'POST'])
def spelling_page():
    """Form for passing words to word_search method"""
    form = WordsForSheet()
    sentence_list = []
    if form.validate_on_submit():
        words_for_search = form.words.data
        words_for_search = words_for_search.replace(" ", "")
        words_for_search = words_for_search.replace(",", "+")
        return redirect(url_for('worksheets.word_search', words=words_for_search))
    return render_template('wordsearch.html', sample_sentences=sentence_list, form=form)

@worksheets.route('/worksheet/<string:words>')
def word_search(words):
    """Find a sentence for each word in the route. If sentences not in db,
    redirect to the sentence adder page, passing in the words not in db
    """
    sentence_list = [[], []]
    words_list = words.split('+')
    words_for_page = words.replace('+', ', ')
    words_not_in_db = ''
    for word in words_list:
        six_words = SixWordsWithBlanks()
        sentence_list[0].append(six_words.generate_six_words_with_blanks(word))
        string_to_query_in_middle = f"% {word} %"
        sentence = Sentence.query.filter(Sentence.sentence.like(string_to_query_in_middle)).first()
        if sentence:
            sentence_with_blanks = ExampleSentence(sentence.sentence)
            sentence_with_blanks.sentence = \
            sentence_with_blanks.remove_space_before_and_after_punct(\
            [",", ".", "!", "?", '"'])
            sentence_list[1].append(sentence_with_blanks.blank_out_word_in_sentence(word))
        else:
            words_not_in_db += word + "+"
    if words_not_in_db:
        return render_template('worksheet.html', sample_sentences=sentence_list,\
        words=words_for_page)
    else:
        words_not_in_db = words_not_in_db[:-1]
        return redirect(url_for('worksheets.sentence_adder', words_to_add=words_not_in_db))

@worksheets.route('/sentence/<string:words_to_add>', methods=['GET', 'POST'])
@login_required
def sentence_adder(words_to_add):
    """Add new sentence to db"""
    form = NewSentence()
    if form.validate_on_submit():
        sentence_to_add_to_db = ExampleSentence(form.sentence.data)
        sentence = " " + sentence_to_add_to_db.add_space_before_and_after_punct(\
        [",", ".", "!", "?", '"'])
        sentence = Sentence(sentence=sentence, user_id=current_user.id)
        db.session.add(sentence)
        db.session.commit()
        flash('Your sentence has been added', 'success')
        return redirect(url_for('worksheets.spelling_page'))
    return render_template('sentence_adder_page.html', title='sentence_adder',\
    form=form, words_to_add=words_to_add)

@worksheets.route('/sentence/delete_page/<string:word>', methods=['GET', 'POST'])
def find_sentence_to_delete(word):
    """Find sentence in db to delete given word"""
    string_to_query_in_middle = f"% {word} %"
    sentence = Sentence.query.filter(Sentence.sentence.like(string_to_query_in_middle)).first()
    if sentence:
        sentence_with_blanks = ExampleSentence(sentence.sentence)
        sentence.sentence = sentence_with_blanks.remove_space_before_and_after_punct(\
        [",", ".", "!", "?", '"'])
        return render_template('delete_sentence_page.html', sample_sentence=sentence)
    else:
        return render_template("home.html")

@login_required
@worksheets.route('/sentence/delete/<int:sentence_id>', methods=['POST'])
def delete_sentence(sentence_id):
    """Delete sentence from db"""
    sentence = Sentence.query.get_or_404(sentence_id)
    db.session.delete(sentence)
    db.session.commit()
    flash('The sentence has been deleted!', 'success')
    return render_template("home.html")
