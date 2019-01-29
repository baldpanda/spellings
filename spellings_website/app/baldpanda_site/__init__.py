from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5b15f64dade99ceb17ee15983fa4bc80'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login_page'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('PANDA_EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('PANDA_PASSWORD')
mail = Mail(app)

from baldpanda_site.users.routes import users
from baldpanda_site.worksheets.routes import worksheets
from baldpanda_site.main.routes import main

app.register_blueprint(users)
app.register_blueprint(worksheets)
app.register_blueprint(main)
