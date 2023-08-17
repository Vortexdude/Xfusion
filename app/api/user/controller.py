from .model import UserModel

class UserController:
    
    @classmethod
    def fetch_users(cls):
        return {"users": UserModel.fetch_all_users()}
     
    @staticmethod
    def create_user(users_data):
        if UserModel.find_by_email(users_data['email']):
            return {"message": "User already present on the database with {} email".format(users_data['email'])}
        user = UserModel(**users_data)
        user.save_to_db()
        return {"message": "User created succesfully you can login now!"}
    
    @staticmethod
    def delete_user(user_id):
        user =  UserModel.find_by_id(user_id['userid'])
        if not user:
            return {"message": "Can not find the user"}
        else:
            user.delete_from_db()
            return {"message": "User Deleted succesfully"}
