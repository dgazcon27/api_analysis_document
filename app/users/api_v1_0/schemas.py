from marshmallow import fields
from app.ext import ma

class UserSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	name = fields.String()
	lastname = fields.String()
	birthday = fields.String()
	direction = fields.String()
	email = fields.String()
	username = fields.String()
