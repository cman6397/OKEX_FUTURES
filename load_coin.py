from app import app
from app.models import Coin_Price
from app import db
from app.okex import okex
import traceback

bitcoin_price ='https://www.okex.com/api/spot/v3/instruments/BTC-USDT/ticker'
method = 'GET'
bitcoin = okex(bitcoin_price,method)
data = bitcoin.get()

btc_price = Coin_Price()
btc_price.instrument = data['instrument_id']
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
