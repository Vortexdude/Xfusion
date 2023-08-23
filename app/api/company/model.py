from app.database.db import db
from sqlalchemy.sql import func
from uuid import uuid4

class CompanyModel(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    legal_entity_key = db.Column(db.String(255), nullable=True)
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
        self.legal_entity_key = str(uuid4())
        self.legal_entity_name = legal_entity_name
        self.status = status
        self.location = location
        self.account_type = account_type
        self.create_by = create_by
        self.assets = assets
        self.description = description

    def to_json(self):
        return {
            "id": self.legal_entity_key,
            "legal_entity_name": self.legal_entity_name,
            "status": self.status,
            "location": self.location,
            "account_type": self.account_type,
            "assets": self.assets,
            "description": self.description,
            "created_by": self.create_by
        }

    @classmethod
    def fetch_all(cls):
        compnies = cls.query.all()
        compnies_list = [
            {
                "name": company.legal_entity_name,
                "status": company.status,
                "location": company.location,
                "created_by": company.create_by,
                "id": company.legal_entity_key,
                "status": company.status,
                "last_modified_time": company.create_timestamp

            }
            for company in compnies
        ]
        return compnies_list

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def fetch_record_by_id(cls, id):
        return cls.query.filter_by(legal_entity_key=id).first()

    @classmethod
    def fetch_record_by_name(cls, name):
        return cls.query.filter_by(legal_entity_name=name).first()

    @classmethod
    def update_record(cls, id=None, legal_entity_name=None, account_type=None, status=None, location=None, logged_in_user=None):
        company = cls.query.filter_by(legal_entity_key=id).first()
        if company:
            if legal_entity_name is not None:
                company.legal_entity_name = legal_entity_name
            if account_type is not None:
                company.account_type = account_type
            if status is not None:
                company.status = status
            if location is not None:
                company.location = location
            if logged_in_user is not None:
                company.updated_by = logged_in_user

            db.session.commit()
            return True
        else:
            return False

    def __repr__(self):
        """String representation of the Class for Debuging persose"""
        
        return f'<Company name {self.legal_entity_name}>'
