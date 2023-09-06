from marshmallow import Schema
from flask_smorest.fields import Upload
from flask_smorest import Blueprint
from flask.views import MethodView
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os
from uuid import uuid4
from app.common.paths import dir
from .controller import convert_to_pdf
dir = dir()

class ImageUpload(Schema):
    file = Upload()

blp = Blueprint("Image_converter", __name__, description="Convert Image into other formats")

@blp.route("/convert_to_pdf")
class PDFConverter(MethodView):

    @blp.arguments(ImageUpload, location="files")
    def post(self, file):
        if not file:
            return {"message": "File not found"}
        _file = file['file']
        filename = str(_file.filename).replace(" ", "_")
        _file.save(os.path.join(dir.output, secure_filename(filename)))
        output_file_name = f"{uuid4()}.pdf"
        try:
            convert_to_pdf(filename, output_file_name)
            return send_from_directory(dir.output, output_file_name)
        except Exception as e:
            return {"message": str(e)}
