import uuid
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError
from db import db
from lib.models import UserModel
from schema import UserSchema

blp = Blueprint("users", __name__, description="Users Operations")
 
@blp.route("/users")
class Users(MethodView):
    def get(self):
        gusers = []
        users = UserModel.query.all()
        for user in users:
            gusers.append({
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "email": user.email,
                })
        return {"users": gusers}
    
    @blp.arguments(UserSchema)
    def post(self, users_data):
        user_id = uuid.uuid4()
        user = UserModel(**users_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            return {"message": "User is already present in the database"}
        return {"users": "User created succesfully you can login now!"}
    