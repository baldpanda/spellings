from baldpanda_site import app, db
from baldpanda_site.models import Sentence, User
from baldpanda_site.example_sentence import Example_sentence
import os

data_path = os.path.join(os.getcwd(), 'sentences.txt')
text_file = open(data_path, "r+")
sentence = ""
sentence_obj = Example_sentence(sentence)
for sentence in text_file:
    sentence = sentence.rstrip()
    sentence_obj.sentence = " " + sentence
    sentence = sentence_obj.add_space_before_and_after_punct([",", ".", "!", "?", '"', "'"])
    sentence_to_add = Sentence(sentence = sentence, user_id = 1)
    db.session.add(sentence_to_add)
    db.session.commit()
