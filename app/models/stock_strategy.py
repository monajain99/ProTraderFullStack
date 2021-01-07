# from .db import db
# from datetime import datetime
# from ..models.user import User
# from ..models.stock import Stock

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship


# class StockStrategies(db.Model):
#   __tablename__ = 'stock_strategies'

#   id = db.Column(db.Integer, primary_key = True)
#   user_id = db.Column(db.ForeignKey("users.id"), db.Integer, nullable=False)
#   stock_id = db.Column(db.ForeignKey("stocks.id"), db.Integer, nullable=False)

#   stocks = db.relationship("Stock", back_populates="stock_price_minutes", cascade="all")
#   strategies = db.relationship("Strategy", back_populates="strategies", cascade="all")
#   users = db.relationship("User", back_populates="stock_price_minutes", cascade="all")


# def to_dict(self):
#         return {
#           "id": self.id,
#           "user_id": len(self.users),
#           "stock_id": len(self.stocks)
#         }