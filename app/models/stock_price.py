from .db import db
from datetime import datetime
from .user import User
from .stock import Stock

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


class StockPrice(db.Model):
  __tablename__ = 'stock_prices'

  id = db.Column(db.Integer, primary_key = True)
  datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  open = db.Column(db.Integer, nullable = False) 
  high = db.Column(db.Integer, nullable = False)
  low = db.Column(db.Integer, nullable = False)
  close = db.Column(db.Integer, nullable = False)
  volume = db.Column(db.Integer, nullable = False)
  stock_id = db.Column(db.ForeignKey("stocks.id"))

  stocks = db.relationship("Stock", back_populates="stock_prices", cascade="all")
  


def to_dict(self):
        return {
          "id": self.id,
          "datetime": self.datetime,
          "open": self.open,
          "high": self.high,
          "low": self.low,
          "close": self.close,
          "volume": self.volume,
          "stock_id": len(self.stocks)
        }


# many stock_price one stocks
