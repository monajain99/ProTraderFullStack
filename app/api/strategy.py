from .db import db
from datetime import datetime
from ..models.user import User

CREATE TABLE strategy (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL
 );
CREATE TABLE stock_strategies (
    stock_id INTEGER NOT NULL,
    strategy_id INTEGER NOT NULL,
    FOREIGN KEY (stock_id) REFERENCES stock (id),
    FOREIGN KEY (strategy_id) REFERENCES strategy (id)
 );