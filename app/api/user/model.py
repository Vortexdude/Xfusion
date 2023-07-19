from app.database.db import db
from uuid import uuid4

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(255), nullable=True, primary_key=True, default=str((lambda: uuid4())()))
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f"<Users {self.fname}>"
    