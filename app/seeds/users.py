from werkzeug.security import generate_password_hash
from app.models import db, User

# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(username='Demo', full_name='Demo User', email='demo@aa.io', buying_power=10000000 ,
                password='password')
    watchlist = Watchlist(name = "watchlist")
    watchlistContent = WatchlistContent(watchlistId = 1, stockId = 1)

    db.session.add(demo)
    db.session.add(watchlist)
    db.session.add(watchlistContent)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_users():
    db.session.execute('TRUNCATE users;')
    db.session.execute('TRUNCATE watchlists;')

    db.session.commit()
