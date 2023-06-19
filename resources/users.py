import uuid
from flask.views import MethodView
from flask_smorest import Blueprint
from schema import UserSchema
from lib.controller.user import UserController

blp = Blueprint("Users", __name__, description="Users Operations")

#define the routes and call the controller
# for a single endpoint I have defined two methods GET and POST
@blp.route("/users")
class Users(MethodView):
    def get(self):
        return UserController.fetch_users()
    
    @blp.arguments(UserSchema)
    def post(self, users_data):
        return UserController.store_user(users_data)
    