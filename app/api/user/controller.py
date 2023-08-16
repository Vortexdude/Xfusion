from .model import UserModel

class UserController:
    
    @classmethod
    def fetch_users(cls):
        _users = []
        users = UserModel.query.all()
        for user in users:
            _users.append({
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "email": user.email,
                })
        return {"users": _users}    
    @staticmethod
    def create_user(users_data):
        # user = "check the user is present or not then create the user so the new error will gone"
        response = UserModel.create_record(users_data)
        message = "User is already present in the database" if response else "User created succesfully you can login now!"
        return {"message": message}
    
    @staticmethod
    def delete_user(user_id):
        id = user_id['userid']
        response = UserModel.delete_record(id)
        message = "Succesfully Deleted the user" if response else "User_id Doesn't exist"
        return {"message": message}
