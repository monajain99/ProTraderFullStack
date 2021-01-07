from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


class EditForm(FlaskForm):
    image_url = StringField('Image')
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    full_name = StringField('Name')
    about = StringField('About')
    buying_power = StringField('Initial Investment', validators=[IntegerField()])
    submit = SubmitField('Update')
    