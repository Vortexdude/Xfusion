from app.database.db import db
from .model import RollModel

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
        modeldata = RollModel(**rolldata)
        try:
            db.session.add(modeldata)
            db.session.commit()
            return {"Message": "Record inserted succesfully!"}
        except Exception as e:
            return {"Message": f"There is an error in the queries{e}"}

    @classmethod
    def update_role(cls, rolldata):
        record = RollModel.query.filter(RollModel.id == rolldata['id']).first()
        if record is not None:
            if "name" in record.__dict__:
                record.name = rolldata['name']

            if "version" in record.__dict__:
                record.version = rolldata['version']

            if "permissions" in record.__dict__:
                record.permissions = rolldata['permissions']
        try:
            db.session.commit()
            return {"Message": "Record Updated succesfully!"}
        except Exception as e:
            return {"Message": f"There is an error in the queries{e}"}

    @classmethod
    def delete_role(cls, rolldata):
        record = RollModel.query.filter(RollModel.id == rolldata['id']).first()
        if record is not None:
            db.session.delete(record)
        try:
            db.session.commit()
            return {"Message": "Record Deleted succesfully!"}
        except Exception as e:
            return {"Message": f"There is an error in the queries{e}"}
