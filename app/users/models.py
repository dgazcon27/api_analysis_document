from app.db import db, BaseModelMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, BaseModelMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	lastname = db.Column(db.String(255))
	email = db.Column(db.String(255), unique=True, nullable=False)
	username = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255), nullable=False)
	birthday = db.Column(db.String(255))
	direction = db.Column(db.String(255))
	auth = db.relationship("Auth", uselist=False, cascade='all, delete-orphan')

	def __init__(self, name="", lastname="", birthday="", direction="", password="", email="", username=""):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday
		self.direction = direction
		self.email = email
		self.password = password
		self.username = username

	def __repr__(self):
		return f'User({self.name})'

	def __str__(self):
		return f'{self.name}'

	def set_password(self, password):
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def get_user(email):
		return User.query.filter(db.or_(User.username==email, User.email==email)).first()