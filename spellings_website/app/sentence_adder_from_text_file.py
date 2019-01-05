from baldpanda_site import app, db
from baldpanda_site.models import Sentence, User
import os

data_path = os.path.join(os.getcwd(), 'sentences.txt')
text_file = open(data_path, "r+")
sentence = ""
for sentence in text_file:
    sentence_to_add = Sentence(sentence = sentence.rstrip(), user_id = 1)
    db.session.add(sentence_to_add)
    db.session.commit()
