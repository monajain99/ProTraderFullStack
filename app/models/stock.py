from .db import db
from datetime import datetime
from .user import User
# from ..models.stock_price import StockPrice

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

class Stock(db.Model):
  __tablename__ = "stocks"

  id = db.Column(db.Integer, primary_key=True)
  ticker = db.Column(db.String(10), nullable=False)
  
  stock_prices = db.relationship("StockPrice", back_populates="stocks", cascade="all")
  
  stock_price_minutes = db.relationship("StockPriceMinute", back_populates="stocks", cascade="all")
 
  # stocks = db.relationship("Stock", back_populates="watchlists", cascade="all")

def to_dict(self):
        return {
          "id": self.id,
          "ticker": self.ticker,
          "name": self.name,
          "exchange": self.exchange,
        }

class Stocklist(db.Model):
  __tablename__ = "stocklists"

  id = db.Column(db.Integer, primary_key=True)
  stockId = db.Column(db.Integer, db.ForeignKey("stocks.id"))
  userId = db.Column(db.Integer, db.ForeignKey("users.id"))
  shares = db.Column(db.Numeric)
  user = db.relationship("User")
  stock = db.relationship("Stock")

class Trade(db.Model):
  __tablename__ = "trades"

  id = db.Column(db.Integer, primary_key=True)
  ticker = db.Column(db.String(10), nullable=False)
  price = db.Column(db.Numeric)
  shares = db.Column(db.Numeric, nullable=False)
  buy = db.Column(db.Boolean)
  buyDate = db.Column(db.DateTime, nullable=False)
  userId = db.Column(db.Integer, db.ForeignKey("users.id"))
  user = db.relationship("User")


# one stock in many watchlist
# one stock in many stock_prices
# one stock in many stock_prices_min
