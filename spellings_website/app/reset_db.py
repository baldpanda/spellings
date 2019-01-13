from baldpanda_site import db
from baldpanda_site.models import User, Sentence

db.drop_all()
db.create_all()
