import os

class Config:
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  SQLALCHEMY_ECHO = True
  API_KEY = 'PK0CDPFB1RM8SA4URUGW'
  SECRET_KEY = 'Z8StsoZwwKFH0TLnJL8LvMfyyI6otN7bkEocWQZe'
  API_URL = 'https://paper-api.alpaca.markets'