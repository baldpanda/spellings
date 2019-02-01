from baldpanda_site.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login_page'
login_manager.login_message_category = 'info'
mail = Mail(app)

from baldpanda_site.users.routes import users
from baldpanda_site.worksheets.routes import worksheets
from baldpanda_site.main.routes import main

app.register_blueprint(users)
app.register_blueprint(worksheets)
app.register_blueprint(main)
