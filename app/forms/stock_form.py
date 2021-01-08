from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Stock


class AddStockForm(FlaskForm):
    image_url = StringField('Image')
    symbol = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    exchange = StringField('exchange', validators=[DataRequired()])
    