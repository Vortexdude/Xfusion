import hashlib
from app.database.db import db
from uuid import uuid4
from app.common.docs import UserJson

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(255), nullable=True, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    # company = db.relationship('CompanyModel', backref='users')

    def __init__(self, fname, lname, email, password):
        self.id = str(uuid4())
        self.fname = fname
        self.lname = lname
        self.email = email
        _encoded_password_in_hex = hashlib.md5(password.encode())
        _encoded_password = _encoded_password_in_hex.hexdigest()
        self.password = _encoded_password

    def to_json(self) -> UserJson:
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "email": self.email
        }

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def auth(cls, email, password):
        encoded_password_in_hex = hashlib.md5(password.encode())
        encoded_password = encoded_password_in_hex.hexdigest()
        return cls.query.filter_by(email=email, password=encoded_password).first()
    
    @classmethod
    def fetch_all_users(cls) -> list:
        users = cls.query.all()
        users_list = [
            {
                "id": user.id,
                "email": user.email,
                "fname": user.fname,
                "lname": user.lname
            } 
            for user in users
            ]
        return users_list

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def __repr__(self) -> str:
        """String representation of the Class for Debuging persose"""
        
        return f"<Users {self.fname}>"
    