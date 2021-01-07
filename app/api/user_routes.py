from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User
# from app.forms import EditForm

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


# @user_routes.route('/<int:id>', methods=['PUT'])
# @login_required
# def update_user(id):
#     form = EditForm()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     user = User.query.get(id)
#     data = request.json
#     if form.data['username']:
#         user.username = data['username']
#     if form.data['email']:
#         user.email = data['email']
#     if form.data['about']:
#         user.full_name = data['about']
#     if form.data['image_url']:
#         user.image_url = data['image_url']
#     db.session.commit()
#     return user.to_dict()