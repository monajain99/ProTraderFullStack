from .db import db
from datetime import datetime

# from ..models.stock_price import StockPrice

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

class Strategy(db.Model):
  __tablename__ = 'strategies'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.Text, nullable=False)

def to_dict(self):
        return {
          "id": self.id,
          "name": self.name,
        }