from .model import UserModel
from uuid import uuid4
from app.database.db import db
from sqlalchemy.exc import SQLAlchemyError

class UserController:
    users = []
    
    @classmethod
    def fetch_users(cls):
        users = UserModel.query.all()
        for user in users:
            UserController.users.append({
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "email": user.email,
                })
        return {"users": UserController.users}    
    @staticmethod
    def store_user(users_data):
        user_id = uuid4()
        user = UserModel(**users_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            return {"message": "User is already present in the database"}
        return {"users": "User created succesfully you can login now!"}
    
    @staticmethod
    def delete_user(user_id):

         if bool(UserModel.query.filter_by(id=user_id['userid']).delete()):
            db.session.commit()
            return {"Message": "Succesfully Deleted the user"}
         else:
            return {"Message": "Incorrect User id"}