from flask_restx import fields

model = {
    'id': fields.Integer(readonly=True, description='The User unique identifier'),
    'firstname': fields.String(required=True, description='User firstname'),
    'lastname': fields.String(required=True, description='User lastname'),
    'email': fields.String(required=True, description='User Email')
}