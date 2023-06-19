from flask_smorest import Blueprint
from flask.views import MethodView
from schema import LoginSchema
from lib.controller import UserController

blp = Blueprint("Authentication", __name__, description="Auth operations")

@blp.route("/login")
class Login(MethodView):

    @blp.arguments(LoginSchema)
    def post(self, logindata):
        return UserController.login(logindata)
        
@blp.route("/logout")
class Logout(MethodView):
    def get(self):
        # return {"messages": "Logout Success!"}
        return UserController.logout()
