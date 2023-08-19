from .model import UserModel
from conf.config_const import CONF

class UserController:
    
    @staticmethod
    def fetch_users():
        return {"users": UserModel.fetch_all_users()}
     
    @staticmethod
    def create_user(users_data):
        email = users_data['email']
        if UserModel.find_by_email(email):
            return {"message": CONF['user_already_exist'].format(email=email)}

        user = UserModel(**users_data)
        user.save_to_db()
        return {"message": CONF['user_created']}

    @staticmethod
    def delete_user(user_id):
        user =  UserModel.find_by_id(user_id)

        if not user:
            return {"message": CONF['user_not_found']}

        user.delete_from_db()
        return {"message": CONF['user_deleted']}
