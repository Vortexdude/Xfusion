from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint
from lib.models import UserModel
from resources.auth.jwt import Jwt
blp = Blueprint("DCIM", __name__, description="DCIM, Auth required")



def token_required(func):
    def wrapper(*args, **kwargs):
        token = None
        if "Bearer" in str(request.headers):
            token = request.headers.get('Authorization').split(" ")[1]
        if not token:
            return {"message": "Token is missing from header"}
        # try:
        #     data = Jwt.decode(token)
        #     current_user = UserModel.query.filter(UserModel.email == data['sub']['email']).first()
        # except:
        #     return {"message": "Invalid token"}
        return Jwt.decode(token)

        return func(current_user, *args, **kwargs)
    return wrapper

@blp.route("/dcim")
class Dcim(MethodView):

    @token_required
    def get(self, current_user):
        return {"message": "protected route", "current_user": current_user.fname}
        
        