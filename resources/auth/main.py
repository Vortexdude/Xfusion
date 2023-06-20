from flask_smorest import Blueprint
from flask.views import MethodView
from schema import LoginSchema
from lib.controller.main import AuthController
from flask_jwt_extended import jwt_required

blp = Blueprint("Authentication", __name__, description="Auth operations")

@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema)
    def post(self, logindata):
        return AuthController.login(logindata)

@blp.route("/logout")
class Logout(MethodView):

    @jwt_required()    
    def get(self):
        return AuthController.logout()
