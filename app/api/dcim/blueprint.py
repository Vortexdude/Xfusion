from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

blp = Blueprint("DCIM", __name__, description="DCIM, Auth required")

@blp.route("/dcim")
class Dcim(MethodView):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"message": "protected route", "current_user": current_user['fname']}
