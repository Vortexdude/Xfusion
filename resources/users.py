import uuid
from flask.views import MethodView
from flask_smorest import Blueprint
from schema import UserSchema
from lib.controller.user import UserController

blp = Blueprint("users", __name__, description="Users Operations")
 
@blp.route("/users")
class Users(MethodView):
    def get(self):
        return UserController.fetch_users()
    
    @blp.arguments(UserSchema)
    def post(self, users_data):
        return UserController.store_user(users_data)
    