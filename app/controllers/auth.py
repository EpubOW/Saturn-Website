from config import *

from flask import Flask, request, Response, render_template, redirect, url_for



# Predefined users dictionary with hashed passwords
users = {
    'admin': bcrypt.generate_password_hash('ask226226').decode('utf-8')
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

def check_auth(username, password):
    """This function is called to check if a username/password combination is valid."""
    if username in users and bcrypt.check_password_hash(users[username], password):
        return True
    return False

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your login!', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    user = User(auth.username)
    login_user(user)
    return redirect(url_for('newPostPage'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('getMain'))


