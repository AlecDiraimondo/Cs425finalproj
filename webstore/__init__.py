from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager

app = Flask(__name__)

#change postgres password to your own when running otherwise authentication will fail
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:proton09@localhost/OnlineGroceryStore'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

db = SQLAlchemy(app)

login_manager = LoginManager(app)

from webstore import routes
