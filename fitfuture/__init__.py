from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '19d70cf654f454f10779a1290e13261f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.app_context().push()
db.create_all()

from fitfuture import routes