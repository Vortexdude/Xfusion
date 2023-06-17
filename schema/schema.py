from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    fname = fields.Str(required=True)
    lname = fields.Str(required=True)
    email = fields.Str(required=True)
    access = fields.Str(required=True)
    