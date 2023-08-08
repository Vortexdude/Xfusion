from .model import RollModel

data = {}
class PermController():
    roles = []

    @classmethod
    def fetch_roles(cls):
        cls.roles = []
        data = RollModel.query.all()
        for role in data:
            cls.roles.append({
                "name": role.name,
                "id": role.id,
                "permissions": role.permissions,
                "version": role.version,
                "create_timestamp": role.create_timestamp,
            })
        return {"roles": cls.roles}

    @classmethod
    def create_role(cls, rolldata):

        response = RollModel.create_record(rolldata)
        data['message'] = "Record inserted succesfully" if response else "There are some eror in the query"
        return data

    @classmethod
    def update_role(cls, rolldata):
        response = RollModel.update_record(rolldata)
        data['message'] = "Record Updated succesfully!" if response else "There is an error in the queries"
        return data

    @classmethod
    def delete_role(cls, rolldata):
        response = RollModel.delete_record(rolldata)
        data['message'] = "Record Deleted succesfully!" if response else "There is an error in the queries{e}"
        return data
