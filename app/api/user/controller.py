from .model import UserModel

USER_ALREADY_EXIST = "User already present on the database with <{email}>"
USER_CREATED_SUCCESFULLY = "User created succesfully you can login now!"
USER_NOT_FOUND = "Can not find the user"
USER_DELETED = "User Deleted succesfully"

class UserController:
    
    @staticmethod
    def fetch_users():
        return {"users": UserModel.fetch_all_users()}
     
    @staticmethod
    def create_user(users_data):
        email = users_data['email']
        if UserModel.find_by_email(email):
            return {"message": USER_ALREADY_EXIST.format(email=email)}

        user = UserModel(**users_data)
        user.save_to_db()
        return {"message": USER_CREATED_SUCCESFULLY}

    @staticmethod
    def delete_user(user_id):
        user =  UserModel.find_by_id(user_id['userid'])

        if not user:
            return {"message": USER_NOT_FOUND}

        user.delete_from_db()
        return {"message": USER_DELETED}
