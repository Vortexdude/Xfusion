from .model import RoleModel
from conf.config_const import CONF

class PermController():

    @classmethod
    def fetch_roles(cls):
        roles_list = RoleModel.fetch_all()
        return {"roles": roles_list}

    @classmethod
    def get_role(cls, role_id):
        role = RoleModel.find_by_id(role_id)
        if not role:
            return {"message": CONF['key_not_found']}        
        return role.to_json()

    @classmethod
    def create_role(cls, roledata):
        role_name = roledata['name']
        role = RoleModel.find_by_name(role_name)
        if role:
            return {"message": CONF['role_already_exist']}
        try:
            role = RoleModel(**roledata)
            role.save_to_db()
            return {"id": role.to_json()['id']}
        except Exception as e:
            return {"message": CONF['query_error'].format(e)}

    @classmethod
    def update_role(cls, roledata, role_id):
        response = RoleModel.update_record(**roledata, id=role_id)
        if response:
            return {"message": CONF['role_updated']}
        else:
            return {"message": CONF['role_not_exist']}

    @classmethod
    def delete_role(cls, role_id):
        role = RoleModel.find_by_id(id=role_id)
        if role:
            try:
                role.delete_from_db()
                return {"message": CONF['role_deleted']}
            except Exception as e:
                return {"message": CONF['query_error'].format(e)}
        else:
            {"message": CONF['role_not_exist']}
