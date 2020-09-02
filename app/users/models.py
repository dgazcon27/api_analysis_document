from app.db import db, BaseModelMixin

class User(db.Model, BaseModelMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256))
	lastname = db.Column(db.String(256))
	birthday = db.Column(db.String(256))
	direction = db.Column(db.String(256))


	def __init__(self, name, lastname, birthday, direction):
		self.name = name
		self.lastname = lastname
		self.birthday = birthday
		self.direction = direction

	def __repr__(self):
		return f'User({self.name})'

	def __str__(self):
		return f'{self.name}'
