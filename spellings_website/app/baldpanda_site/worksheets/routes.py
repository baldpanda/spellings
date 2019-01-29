from baldpanda_site import app, db
from baldpanda_site.example_sentence import Example_sentence
from baldpanda_site.worksheets.forms import  WordsForSheet, NewSentence
from baldpanda_site.models import Sentence
from baldpanda_site.six_words_with_spaces import Six_words_with_blanks
from flask import render_template, url_for, redirect, request, Blueprint, flash
from flask_login import login_required

worksheets = Blueprint('worksheets', __name__)

@worksheets.route('/worksheet', methods = ['GET', 'POST'])
def spelling_page():
    form = WordsForSheet()
    sentence_list = []
    if form.validate_on_submit():
        words_for_search = form.words.data
        words_for_search = words_for_search.replace(" ", "")
        words_for_search = words_for_search.replace(",", "+")
        return redirect(url_for('worksheets.word_search', words = words_for_search))
    return render_template('wordsearch.html', sample_sentences = sentence_list, form = form)

@worksheets.route('/worksheet/<string:words>')
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
        return redirect(url_for('worksheets.sentence_adder', words_to_add=words_not_in_db))

@worksheets.route('/sentence/<string:words_to_add>', methods = ['GET', 'POST'])
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
        return(redirect(url_for('worksheets.spelling_page')))
    return render_template('sentence_adder_page.html', title = 'sentence_adder',
    form = form, words_to_add = words_to_add)
