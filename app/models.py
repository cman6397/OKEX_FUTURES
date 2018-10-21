from app import db
from flask_login import UserMixin
from app import login
from passlib.hash import sha256_crypt

class Coin_Price(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	instrument = db.Column(db.String(), unique=False, nullable=True)
	best_ask = db.Column(db.String(), unique=False, nullable=True)
	best_bid = db.Column(db.String(), unique=False, nullable=True)
	last_price = db.Column(db.String(), unique=False, nullable=True)
	volume_24h = db.Column(db.String(), unique=False, nullable=True)
	timestamp = db.Column(db.String(), unique=False,nullable=True)

	def __repr__(self):
		return '<instrument = %r, best_ask = %r, best_bid = %r, last_price %r, volume_24h %r, timestamp %r>' % (self.instrument, self.best_ask, self.best_bid, self.last_price, self.volume_24h, self.timestamp)
