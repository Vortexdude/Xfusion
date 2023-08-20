from marshmallow import fields, Schema

class PermSchema(Schema):
    id = fields.Str(requeried=True)
    roles = fields.Str(requeried=True)


class RoleSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    version = fields.Str(required=True)
    permissions = fields.Str(required=True)
    global_ultimate_key = fields.Str(required=True)

class UpdateSchema(Schema):
    name = fields.Str(required=False)
    version = fields.Str(required=False)
    permissions = fields.Str(required=False)

class AuthorizationHeaderSchema(Schema):
    Authorization = fields.Str(
        description='Authorization token',
        required=True,
        example='Bearer <your-token-here>'
    )