from baldpanda_site.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from baldpanda_site import create_app

app = create_app()

def reset_db(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from baldpanda_site import db
    db.init_app(app)
    db.drop_all()
    db.create_all()

reset_db()
