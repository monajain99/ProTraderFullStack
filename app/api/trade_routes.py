# from flask import Blueprint, jsonify, json
# import alpaca_trade_api as tradeapi
# from app.config import Config
# from app.models import Stock
# import websocket
# import pandas as pd
# import ta
# from secrets import *



# trade_routes = Blueprint('trade', __name__)

# @trade_routes.route('/')
# def trades():
# # Alpaca API config stuff

#     AUTHENTICATE = {
#         "action": "authenticate",
#         "data": {
#             "key_id": Config.API_KEY,
#             "secret_key": Config.SECRET_KEY
#         }
#     }

#     tickers = ['alpacadatav1/AM.MSFT', 'alpacadatav1/AM.FB']

#     listen = {
#         'action': 'listen', 'data': {'streams': tickers}
#     }


#     def on_open(ws):
#         ws.send(json.dumps(AUTHENTICATE))
#         ws.send(json.dumps(listen))


#     def on_message(ws, minute_bar):

#         ta.ingest_stream(minute_bar)


#     def on_close(ws):
#         print('closed connection')


#     socket = APCA_WEB_SOCKET

#     ws = websocket.WebSocketApp(socket, on_open=on_open,
#                                 on_message=on_message, on_close=on_close)
#     ws.run_forever()

        



