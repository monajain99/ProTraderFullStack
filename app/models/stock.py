from .db import db
from datetime import datetime
from .user import User
# from ..models.stock_price import StockPrice

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

class Stock(db.Model):
  __tablename__ = 'stocks'

  id = db.Column(db.Integer, primary_key = True)
  symbol = db.Column(db.Text, nullable=False)
  name = db.Column(db.Text, nullable=False)
  exchange = db.Column(db.Text, nullable=False)
  
  stock_prices = db.relationship("StockPrice", back_populates="stocks", cascade="all")
  
  stock_price_minutes = db.relationship("StockPriceMinute", back_populates="stocks", cascade="all")
 
  # stocks = db.relationship("Stock", back_populates="watchlists", cascade="all")

def to_dict(self):
        return {
          "id": self.id,
          "symbol": self.symbol,
          "name": self.name,
          "exchange": self.exchange,
        }


# one stock in many watchlist
# one stock in many stock_prices
# one stock in many stock_prices_min
