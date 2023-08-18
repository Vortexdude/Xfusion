from .model import RollModel

ROLE_ALREADY_EXIST = "Role already exist in the database please use that or change the role name."
ROLE_INSERTED_SUCCESFULL = "Record created succesfully!"
ROLE_ID_MISSING = "Role ID is missing, please provide the role ID first"
ROLE_UPDATED_SUCCESSFULLY = "Role Updated succesfully!"
ROLE_NOT_EXIST = "The role is not Exist on the database"
ROLE_DELETED_SUCCESFULLY = "Role Deleted successfully!"
ROLE_QUERY_ERROR = "There was an error in the queries: {e}"

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
            message = ROLE_ALREADY_EXIST
        else:
            role = RollModel(**roledata)
            role.save_to_db()
            message = ROLE_INSERTED_SUCCESFULL
        return {"message": message}

    @classmethod
    def update_role(cls, roledata):
        if "id" not in roledata:
            return {"message": ROLE_ID_MISSING}
        response = RollModel.update_record(**roledata)
        if response:
            message = ROLE_UPDATED_SUCCESSFULLY
        else:
            message = ROLE_NOT_EXIST
        return {"message": message}

    @classmethod
    def delete_role(cls, roledata):
        role = RollModel.find_by_id(id=roledata['id'])
        if role:
            try:
                role.delete_from_db()
                message = ROLE_DELETED_SUCCESFULLY
            except Exception as e:
                message = ROLE_QUERY_ERROR.format(e)
        return {"message": message}
