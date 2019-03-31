"""Utility methods to be used by route methods for users"""

from flask import url_for
from flask_mail import Message
from baldpanda_site import mail

def send_reset_email(user):
    """send password reset email from baldpanda email address"""
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='baldpanda94@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password please visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not request this email, please ignore.
    '''
    mail.send(msg)
