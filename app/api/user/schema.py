from marshmallow import Schema, fields

class UserDelSchema(Schema):
    userid = fields.Int(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
