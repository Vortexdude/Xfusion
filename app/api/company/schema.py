from marshmallow import Schema, fields

class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    legal_entity_name = fields.Str(required=True)
    status = fields.Str(required=True)
    account_type = fields.Str(required=True)
    location = fields.Str(required=True)

class CompanyUpdateSchema(Schema):
    legal_entity_name = fields.Str(required=False)
    status = fields.Str(required=False)
    account_type = fields.Str(required=False)
    location = fields.Str(required=False)
