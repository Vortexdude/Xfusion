from app.database.db import db
from uuid import uuid4

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(255), nullable=True, primary_key=True, default=str((lambda: uuid4())()))
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    # company = db.relationship('CompanyModel', backref='users')

    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def json(self):
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
        return cls.query.filter_by(email=email, password=password).first()
    
    @classmethod
    def fetch_all_users(cls):
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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f"<Users {self.fname}>"
    