from marshmallow import fields, Schema

class PermSchema(Schema):
    id = fields.Int(requeried=True)
    roles = fields.Str(requeried=True)


class RollSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    version = fields.Str(required=True)
    permissions = fields.Str(required=True)
    global_ultimate_key = fields.Str(required=True)
