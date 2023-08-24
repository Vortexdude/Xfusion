from app.database.db import db
from sqlalchemy.sql import func
from uuid import uuid4
from app.common.docs import RoleJson

class RoleModel(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.String(255), nullable=True, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    version = db.Column(db.String(20), nullable=True)
    permissions = db.Column(db.String, nullable=True)
    global_ultimate_key = db.Column(db.String(80), unique=False, nullable=False)
    create_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_modify_time = db.Column(db.DateTime, onupdate=func.now())

    def __init__(self, name=None, version=None, permissions=None, global_ultimate_key=None):
        self.id = str(uuid4())
        self.name = name
        self.version = version
        self.permissions = permissions
        self.global_ultimate_key = global_ultimate_key

    def to_json(self) -> RoleJson:
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "permissions": self.permissions,
            "global_ultimate_key": self.global_ultimate_key
        }
    @classmethod
    def fetch_all(cls):
        roles = cls.query.all()
        role_list = [{
            "id": role.id,
            "name": role.name,
            "version": role.version,
            "permissions": role.permissions,
            "global_ultimate_key": role.global_ultimate_key
        }for role in roles]
        return role_list

    @classmethod
    def find_by_id(cls, role_id):
        return cls.query.filter_by(id=role_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()       


    @classmethod
    def update_record(cls, id=None, name=None, version=None, permissions=None):
        record = cls.query.filter_by(id=id).first()
        if record:
            if name is not None:
                record.name = name
            if version is not None:
                record.version = version
            if permissions is not None:
                record.permissions = permissions
            db.session.commit()
            return True
        else:
            return False
