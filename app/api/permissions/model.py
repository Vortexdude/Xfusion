from app.database.db import db
from sqlalchemy.sql import func
from uuid import uuid4

class RollModel(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.String(255), nullable=True, primary_key=True, default=str((lambda: uuid4())()))
    name = db.Column(db.String(80), unique=True, nullable=False)
    version = db.Column(db.String(20), nullable=True)
    permissions = db.Column(db.String, nullable=True)
    global_ultimate_key = db.Column(db.String(80), unique=False, nullable=False)
    create_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_modify_time = db.Column(db.DateTime, onupdate=func.now())
