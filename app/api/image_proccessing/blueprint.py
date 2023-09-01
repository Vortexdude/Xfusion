from flask import send_from_directory
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
import os
from werkzeug.utils import secure_filename
from .controller import ImageProccessing
from .schema import MultipartFileSchema
from app.common.utils import dir

blp = Blueprint("Image_Proccessing", __name__, description="Proccessing Image using openCV")

dir = dir()

@blp.route("/upload")
class ImageProccessingRoute(MethodView):

    @jwt_required()
    @blp.arguments(MultipartFileSchema, location='files')
    def post(self, file):
        """method used for detecting the face from an image

        Args:
            file (image): the image that need to be filtered

        Returns:
            string or image: return the image with rectangle 
            over the face is not it will return the string
        """
        if not file:
            return {'message': 'Please upload file'}
        _file = file['file']
        _file.save(os.path.join(dir.output, secure_filename(_file.filename)))
        image_name = f"{uuid4()}.jpg"
        try:
            ImageProccessing.detect_face(f"{dir.output}/{_file.filename}", f"{dir.proccesed}/{image_name}")
        except:
            return {"message": "Face not found"}
        return send_from_directory(dir.proccesed, image_name)
