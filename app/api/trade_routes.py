from flask import Blueprint, jsonify
import alpaca_trade_api as tradeapi
from app.config import Config
from app.models import Stock


trade_routes = Blueprint('trade', __name__)

@trade_routes.route('/')
def trades():
    return ('someTrades')
    # api = tradeapi.REST(Config.API_KEY, Config.SECRET_KEY, base_url=Config.API_URL)
    # assets = api.list_assets()
    # return assets
    # for asset in assets:
    #     try:
    #         if asset.status == 'active' and asset.tradable:
    #             print({asset.symbol}, {asset.name}, {asset.exchange})
    #     except Exception as e:
    #         print(asset.symbol)
    #         return(e)

        



