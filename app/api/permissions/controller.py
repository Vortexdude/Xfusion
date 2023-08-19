from .model import RollModel
from conf.config_const import CONF

class PermController():

    @classmethod
    def fetch_roles(cls):
        roles_list = RollModel.fetch_all()
        return {"roles": roles_list}

    @classmethod
    def create_role(cls, roledata):
        role_name = roledata['name']
        role = RollModel.find_by_name(role_name)
        if role:
            message = CONF['role_already_exist']
        else:
            role = RollModel(**roledata)
            role.save_to_db()
            message = CONF['role_created']
        return {"message": message}

    @classmethod
    def update_role(cls, roledata, role_id):
        response = RollModel.update_record(**roledata, id=role_id)
        if response:
            message = CONF['role_updated']
        else:
            message = CONF['role_not_exist']
        return {"message": message}

    @classmethod
    def delete_role(cls, role_id):
        role = RollModel.find_by_id(id=role_id)
        if role:
            try:
                role.delete_from_db()
                message = CONF['role_deleted']
            except Exception as e:
                message = CONF['query_error'].format(e)
        else:
            message = CONF['role_not_exist']
        return {"message": message}
