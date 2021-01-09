from .db import db
from datetime import datetime
from .user import User
from .stock import Stock

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# # one watchlist many stocks
# # one watchlist one user

class Watchlist(db.Model):
  __tablename__ = "watchlists"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))

class WatchlistContent(db.Model):
  __tablename__ = "watchlistContent"
  
  id = db.Column(db.Integer, primary_key=True)
  watchlistId = db.Column(db.Integer, db.ForeignKey("watchlists.id"))
  stockId = db.Column(db.Integer, db.ForeignKey("stocks.id"))
  stock = db.relationship("Stock")
  watchlist = db.relationship("Watchlist")



