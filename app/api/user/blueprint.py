from flask.views import MethodView
from flask_smorest import Blueprint
from .schema import UserSchema, UserDelSchema
from .controller import UserController
from flask_jwt_extended import jwt_required

blp = Blueprint("Users", __name__, description="Users Operations")

#define the routes and call the controller
# for a single endpoint I have defined two methods GET and POST
@blp.route("/users")
class Users(MethodView):

    @jwt_required()
    def get(self):
        return UserController.fetch_users()
    
    @blp.arguments(UserSchema)
    def post(self, users_data):
        return UserController.create_user(users_data)
    
    @jwt_required()
    @blp.arguments(UserDelSchema)
    def delete(self, user_id):
        return UserController.delete_user(user_id)
    