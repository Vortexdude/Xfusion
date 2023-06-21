from app.database.db import db
from sqlalchemy.sql import func

class CompanyModel(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    legal_entity_key = db.Column(db.String(80), unique=True, nullable=False)
    legal_entity_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    account_type = db.Column(db.String(80), nullable=False)
    assets = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    create_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_modify_time = db.Column(db.DateTime, onupdate=func.now())

    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f'<Company name {self.legal_entity_name}>'