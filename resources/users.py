import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from db import users
from schema import UserSchema

blp = Blueprint("users", __name__, description="Users Operations")

@blp.route("/users")
class Users(MethodView):
    def get(self):
        return {"users": users}
    
    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema(many=True))
    def post(self, users_data):
        users_data = request.get_json()
        if users_data["email"] in users.values():
            return {"message": "User already present"}
        user_id = uuid.uuid4()
        new_data = {"id": user_id, **users_data}
        users.update(new_data)
        return new_data
    