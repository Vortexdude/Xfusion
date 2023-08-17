from app.database.db import db
from sqlalchemy.sql import func
from sqlalchemy.exc import SQLAlchemyError
from uuid import uuid4

class CompanyModel(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    legal_entity_key = db.Column(db.String(255), nullable=True, default=str((lambda: uuid4())()))
    legal_entity_name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    account_type = db.Column(db.String(80), nullable=False)
    assets = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    create_timestamp = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_modify_time = db.Column(db.DateTime, onupdate=func.now())
    create_by = db.Column(db.String)
    # create_by = db.Column(db.String, db.ForeignKey('users.id'))
    updated_by = db.Column(db.String, nullable=True, default="")

    def __init__(self, legal_entity_name, status, location, account_type, create_by, assets=None, description=None):
        self.legal_entity_name = legal_entity_name
        self.status = status
        self.location = location
        self.account_type = account_type
        self.create_by = create_by
        self.assets = assets
        self.description = description

    def to_json(self):
        return {
            "id": self.id,
            "legal_entity_name": self.legal_entity_name,
            "status": self.status,
            "location": self.location,
            "account_type": self.account_type,
            "assets": self.assets,
            "description": self.description,
            "created_by": self.create_by
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delte_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def fetch_record_by_id(id):
        company = CompanyModel.query.filter_by(legal_entity_key=id).first()
        return company.name

    @staticmethod
    def update_record(id=None, legal_entity_name=None, account_type=None, status=None, location=None, loggedInUser=None):
        company = CompanyModel.query.filter_by(legal_entity_key=id).first()
        if bool(company):
            if legal_entity_name: company.legal_entity_name
            if account_type: company.account_type = account_type 
            if status: company.status = status
            if location: company.location = location
            if loggedInUser: company.updated_by = loggedInUser 
            db.session.commit()        
            return True
        else:
            return False

    @staticmethod
    def delete_record(key):
        response = CompanyModel.query.filter_by(legal_entity_key=key).delete()
        if bool(response):
            db.session.commit()
            return True
        else:
            False

    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f'<Company name {self.legal_entity_name}>'