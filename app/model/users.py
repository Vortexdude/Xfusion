from app.database.db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Users {self.fname}>"
    