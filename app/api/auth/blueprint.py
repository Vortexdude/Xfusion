from flask_smorest import Blueprint
from flask.views import MethodView
from .schema import LoginSchema
from .controller import AuthController
from flask_jwt_extended import jwt_required

blp = Blueprint("Authentication", __name__, description="Auth operations")

body = {
    'name': 'Authorization', 
    'in': 'header', 
    'description': 'Authorization: Bearer <access_token>', 
    'required': 'true',
    'default': "nothing"
    }
timeout_field = {
    'name': 'timeout', 
    'in': 'header', 
    'description': '3000 #paste your timeout session', 
    'required': 'true',
    'default': "3000"
    }

@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema, location='json')
    @blp.doc(parameters=[timeout_field])
    def post(self, logindata: dict):
        return AuthController.login(logindata)

@blp.route("/logout")
class Logout(MethodView):

    @jwt_required()     
    def get(self):
        return AuthController.logout()
