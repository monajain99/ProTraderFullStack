from flask import Blueprint, jsonify
import alpaca_trade_api as tradeapi
import app.config as config
from app.models import Stock


#   API_KEY = 'PK0CDPFB1RM8SA4URUGW'
#   SECRET_KEY = 'Z8StsoZwwKFH0TLnJL8LvMfyyI6otN7bkEocWQZe'
#   API_URL = 'https://paper-api.alpaca.markets'
#   API_KEY='PK0CDPFB1RM8SA4URUGW'
#   SECRET_KEY='Z8StsoZwwKFH0TLnJL8LvMfyyI6otN7bkEocWQZe'
#   API_URL='https://paper-api.alpaca.markets'

trade_routes = Blueprint('trade', __name__)

@trade_routes.route('/')
def trades():
    api = tradeapi.REST('PK0CDPFB1RM8SA4URUGW', 'Z8StsoZwwKFH0TLnJL8LvMfyyI6otN7bkEocWQZe', "https://paper-api.alpaca.markets")
    # api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)
    assets = api.list_assets()
    for asset in assets:
        try:
            if asset.status == 'active' and asset.tradable:
                print(f" {asset.symbol} {asset.name} {asset.exchange}")
        except Exception as e:
            print(asset.symbol)
            print(e)

        
@trade_routes.route('/stocks')
def stocks():
    stocks = Stock.query.all()
    return {"stocks": [stocks.to_dict() for stock in stocks]}



# @trade_routes.route('/stocks/<int:id>')
# def stocks(id):
#     stock = Stock.query.get(id)
#     return stock.to_dict()



