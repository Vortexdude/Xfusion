from .model import RollModel

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
            message = "Role already Exist please use that or change the role name"
        else:
            role = RollModel(**roledata)
            role.save_to_db()
            message = "Record inserted succesfully"
        return {"message": message}

    @classmethod
    def update_role(cls, roledata):
        if "id" not in roledata:
            return {"message": "Role ID is missing"}
        response = RollModel.update_record(**roledata)
        if response:
            message = "Record Updated succesfully!"
        else:
            message = f"The role is not Exist on the database!"
        return {"message": message}

    @classmethod
    def delete_role(cls, roledata):
        role = RollModel.find_by_id(id=roledata['id'])
        if role:
            try:
                role.delete_from_db()
                message = "Record Deleted successfully!"
            except Exception as e:
                message = f"There was an error in the queries: {e}"
        return {"message": message}
