from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Str(required=True, dump_default="test@email.com")
    password = fields.Str(required=True, dump_default="test")
