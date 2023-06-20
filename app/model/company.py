from app.database.db import db
from sqlalchemy.sql import func

class CompanyModel(db.Model):
    __tablename__ = "assets"
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    legal_entity_key = db.Column(db.String(80), unique=True, nullable=False)
    legal_entity_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(20), unique=True, nullable=False)
    legal_entity_key = db.Column(db.String(80), unique=True, nullable=False)
    account_type = db.Column(db.String(80), unique=True, nullable=False)
    create_timestamp = db.Column(db.DateTime, server_default=func.now())
    last_modify_time = db.Column(db.DateTime, onupdate=func.now())
