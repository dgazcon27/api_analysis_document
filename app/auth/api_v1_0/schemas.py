from marshmallow import fields
from app.ext import ma

class AuthSchema(ma.Schema):
	id = fields.Integer(dump_only=True)
	token = fields.String()
	user_id = fields.Integer()
	create_at = fields.DateTime()
