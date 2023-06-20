from marshmallow import Schema, fields

class CompanySchema(Schema):
    id = fields.Int(dump_only=True)
    legal_entity_key = fields.Str(required=True)
    legal_entity_name = fields.Str(required=True)
    status = fields.Str(required=True)
    account_type = fields.Str(required=True)

