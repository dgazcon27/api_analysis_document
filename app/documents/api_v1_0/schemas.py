from marshmallow import fields
from app.ext import ma


class DocumentsSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    url = fields.String()
    name = fields.String()
    user_id = fields.Integer()
