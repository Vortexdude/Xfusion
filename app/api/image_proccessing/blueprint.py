from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

blp = Blueprint("Image_Proccessing", __name__, description="Proccessing Image using openCV")

@blp.route("/upload")
class ImageProccessing(MethodView):

    @jwt_required()
    def post(self, args):
        current_user = get_jwt_identity()
        return {"message": "protected route", "current_user": current_user['fname']}
