#from tests import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)

app.config['SECRET_KEY']='45968594lkjgnf24958caskcturoty234'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data_base/currency_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Coin_Price(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	instrument = db.Column(db.String(), unique=False, nullable=True)
	best_ask = db.Column(db.String(), unique=False, nullable=True)
	best_bid = db.Column(db.String(), unique=False, nullable=True)
	last_price = db.Column(db.String(), unique=False, nullable=True)
	volume_24h = db.Column(db.String(), unique=False, nullable=True)
	timestamp = db.Column(db.String(), unique=False,nullable=True)

db.create_all()