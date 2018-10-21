from app import app
from app.models import Coin_Price
from app import db
from app.okex import okex
import traceback

def rest_bitcoin():
	bitcoin_price ='https://www.okex.com/api/spot/v3/instruments/BTC-USDT/ticker'
	method = 'GET'
	bitcoin = okex(bitcoin_price,method)
	data = bitcoin.get()
	try:
		assert (data['instrument_id'] == 'BTC-USDT')
		print('Success')

	except Exception:
		print('FAILED')

def add_remove_coin():
	bitcoin_price ='https://www.okex.com/api/spot/v3/instruments/BTC-USDT/ticker'
	method = 'GET'
	bitcoin = okex(bitcoin_price,method)
	data = bitcoin.get()

	btc_price = Coin_Price()
	btc_price.instrument = 'test'
	btc_price.best_ask = data['best_ask']
	btc_price.best_bid = data['best_bid']
	btc_price.last_price = data['last']
	btc_price.volume_24h = data['quote_volume_24h']
	btc_price.timestamp = data['timestamp']

	try:
		db.session.add(btc_price)
		db.session.commit()
	except Exception:
		db.session.rollback()
		print('FAILED: Coin Add Submission Error')
		traceback.print_exc()

	coin_query = db.session.query(Coin_Price).filter(btc_price.instrument == 'test')
	coin_price = coin_query.first()

	try:
		assert(coin_price.instrument == 'test')
	except Exception:
		print('FAILED: Coin Add Verification Error')

	coin_query.delete()

	try:
		print('Success')
		db.session.commit()
	except Exception:
		db.session.rollback()
		print('FAILED: Coin Delete Error')

	try:
		assert (len(coin_query.all()) == 0)
	except Exception:
		print('FAILED: Coin Delete Error')


if __name__ == '__main__':
	rest_bitcoin()
	add_remove_coin()


