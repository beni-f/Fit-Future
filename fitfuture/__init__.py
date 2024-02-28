from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '19d70cf654f454f10779a1290e13261f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///record.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from fitfuture import routes