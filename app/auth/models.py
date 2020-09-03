from app.db import db, BaseModelMixin
from flask_jwt_extended import create_access_token
import datetime

class Auth(db.Model, BaseModelMixin):
	id = db.Column(db.Integer, primary_key=True)
	token = db.Column(db.Text, unique=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now, default=datetime.datetime.now)

	def __init__(self, token, user_id):
		self.token = token
		self.user_id = user_id

	def __str__(self):
		return f'{self.id}'

	def set_token(self, token):
		self.token = token

	def update_auth(self, data):
		return Auth.query.update(preserve_parameter_order=True).where(Auth.id==self.id).values(data)

	def get_by_token(token):
		return Auth.query.filter_by(token=token).first()

	def create_token(self):
		access_token = create_access_token(identity=user.username)