import os

class Config:
    SECRET_KEY = os.environ.get('PANDA_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('PANDA_DB_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('PANDA_EMAIL')
    MAIL_PASSWORD = os.environ.get('PANDA_PASSWORD')
