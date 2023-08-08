from app.database.db import db
from uuid import uuid4

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(255), nullable=True, primary_key=True, default=str((lambda: uuid4())()))
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    company = db.relationship('CompanyModel', backref='users')

    @staticmethod
    def create_record(data):
        user = UserModel(**data)
        if user:
            db.session.add(user)
            db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def update_record():
        pass

    @staticmethod
    def delete_record(key):
        response = UserModel.query.filter_by(id=key).delete()
        if bool(response):
            db.session.commit()
            return True
        else:
            return False
    
    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f"<Users {self.fname}>"
    