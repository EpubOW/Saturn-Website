from flask import Flask, request, json
from time import time
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_cors import CORS, cross_origin
from flask_login import UserMixin, login_user, current_user, logout_user, login_required

app = Flask(__name__, template_folder='resources/templates',  static_folder='resources/static', static_url_path = '')

cors = CORS(app, supports_credentials=True, resources={r"*": {"origins": "*"}})

# bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@localhost:5432/saturn_news'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


# app has been set and configured
sess = Session(app)
db = SQLAlchemy(app)
app.secret_key = 'sdkfp23wisjoifmasmd22343fdfoq23j542rfl1samdkfsfsofijas'
app.config['SESSION_TYPE'] = 'filesystem'


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

sess.init_app(app)