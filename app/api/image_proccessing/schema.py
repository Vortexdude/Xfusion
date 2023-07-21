from marshmallow import Schema, fields
from flask_smorest.fields import Upload

class MultipartFileSchema(Schema):
    file = Upload()
