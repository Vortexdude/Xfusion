from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from .controller import ImageProccessing
from uuid import uuid4
from .schema import MultipartFileSchema
from werkzeug.utils import secure_filename
import os

blp = Blueprint("Image_Proccessing", __name__, description="Proccessing Image using openCV")

class dir:
    def __init__(self):
        self.pwd = os.getcwd()

    @property
    def output(self):
        dir = f"{self.pwd}/output"
        os.makedirs(f"{self.pwd}/output", exist_ok=True)
        return dir

    @property
    def proccesed(self):
        dir = f"{self.pwd}/proccessed"
        os.makedirs(f"{self.pwd}/proccessed", exist_ok=True)
        return dir

dir = dir()

@blp.route("/upload")
class ImageProccessingRoute(MethodView):

    @jwt_required()
    @blp.arguments(MultipartFileSchema, location='files')
    def post(self, file):
        base_dir = os.getcwd()
        _file = file['file']
        _file.save(os.path.join(dir.output, secure_filename(_file.filename)))
        current_user = get_jwt_identity()
        ImageProccessing.detect_face(f"{dir.output}/{_file.filename}", f"{dir.proccesed}/{uuid4()}.jpg")
        return {"message": "protected route", "current_user": current_user['fname']}
