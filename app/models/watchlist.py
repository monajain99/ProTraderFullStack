from .db import db
from datetime import datetime
from .user import User
from .stock import Stock

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

class Watchlist(db.Model):
  __tablename__ = 'watchlists'

  id = db.Column(db.Integer, primary_key = True)
  stock_id = db.Column(db.ForeignKey("stocks.id"))
  user_id = db.Column(db.ForeignKey("users.id"))
  
  watchlists = db.relationship("Stock", back_populates="stocks", cascade="all")
  
  user_id = db.relationship("User", back_populates="users", cascade="all")



def to_dict(self):
        return {
          "id": self.id,
          "user_id": len(self.users),
          "stock_id": len(self.stocks)
        }

# one watchlist many stocks
# one watchlist one user

