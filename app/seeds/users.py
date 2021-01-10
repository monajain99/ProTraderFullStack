from werkzeug.security import generate_password_hash
from app.models import db, User, Watchlist, WatchlistContent, Stock, Stocklist

# Adds a demo user, you can add other users here if you want
def seed_users():

    watchlist = Watchlist(name="watchlist")
    appl = Stock(ticker = "AAPL")

    watchlistContent = WatchlistContent(watchlistId = 21, stockId = 17)

    demo = User(username='Demo', full_name='Demo User', email='demo@aa.io', buying_power=10000000 ,
                password='password', watchlistId = 21)
    watchlistContent = WatchlistContent(watchlistId = 21, stockId = 17)
    stocklist = Stocklist(shares = 3, stockId = 17, userId = 5)

    db.session.add(watchlist)
    db.session.add(appl)
    db.session.add(watchlistContent)
    db.session.add(demo)
    db.session.add(stocklist)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    # db.session.execute('TRUNCATE stocklists CASCADE;')
    # db.session.execute('TRUNCATE users CASCADE;')
    # db.session.execute('TRUNCATE watchlistContent ;')
    # db.session.execute('TRUNCATE stocks CASCADE;')
    # db.session.execute('TRUNCATE watchlists CASCADE;')
    # db.session.execute('TRUNCATE trades CASCADE;')

    db.session.commit()
