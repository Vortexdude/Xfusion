from app.database.db import db
from .model import RollModel

class PermController():
    roles = []

    @classmethod
    def fetch_roles(cls):
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
        modeldata = RollModel(**rolldata)
        try:
            db.session.add(modeldata)
            db.session.commit()
            return {"Message": "Record inserted succesfully!"}
        except Exception as e:
            return {"Message": f"There is an error in the queries{e}"}
