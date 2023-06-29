from marshmallow import Schema, fields

class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
