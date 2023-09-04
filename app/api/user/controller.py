from typing import Dict
from .model import UserModel
from conf.config_const import CONF
from app.common import is_valid_uuid

class UserController:

    @staticmethod
    def fetch_users():
        return {"users": UserModel.fetch_all_users()}

    @staticmethod
    def get_user(id : str) -> None:
        if not is_valid_uuid(id):
            return {"message": CONF['wrong_key']}

        user = UserModel.find_by_id(id)
        if not user:
            return {"message": CONF['key_not_found']}
        return user.to_json()

    @staticmethod
    def create_user(users_data) -> Dict[str, str]:
        email = users_data['email']
        if UserModel.find_by_email(email):
            return {"message": CONF['user_already_exist'].format(email=email)}

        user = UserModel(**users_data)
        try:
            user.save_to_db()
            return {"id": user.to_json()['id']}
        except Exception as e:
            return {"message": str(e)}

    @staticmethod
    def delete_user(user_id):
        user =  UserModel.find_by_id(user_id)

        if not user:
            return {"message": CONF['user_not_found']}

        user.delete_from_db()
        return {"message": CONF['user_deleted']}
