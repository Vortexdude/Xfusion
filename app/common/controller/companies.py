from app.model.company import CompanyModel
from app.database.db import db
from sqlalchemy.exc import SQLAlchemyError
from uuid import uuid4

class CompanyController():
    companies = []

    @classmethod
    def fetch_company(cls):
        companies = CompanyModel.query.all()
        for company in companies:
            cls.companies.append({
                "name": company.legal_entity_name,
                "key": company.legal_entity_key,
                "status": company.status,
                "account_type": company.account_type,
                "create_timestamp": company.create_timestamp,
                "last_modify_time": company.last_modify_time,
                "description": company.description,
                "assetes": company.assets,
                "location": company.location
            })
        return {"compnies": cls.companies}

    @classmethod
    def store_company(cls, company_data):
        legal_entity_key = str(uuid4().hex)
        _data = {"legal_entity_key": legal_entity_key, **company_data}
        model_data = CompanyModel(**_data)
        try:
            db.session.add(model_data)
            db.session.commit()
        except SQLAlchemyError:
            return {"data": "There some issues with the database"}    
            
        return {"data": "inserted succesfully !"}
    
    @classmethod
    def update_company(cls, company_data):
        company = CompanyModel.query.filter_by(legal_entity_name=company_data['legal_entity_name']).update(**company_data)
        # company.account_type = company_data['account_type']
        # company.status = company_data['status']
        # company.location = company_data['location']
        db.session.commit()
        db.session.flush()
        return {"Status": "data Updated succesfully"}
    
    @classmethod
    def delete_company(cls, key):
        CompanyModel.query.filter_by(legal_entity_key=key['legal_entity_key']).delete()
        db.session.commit()        
        return {"Status": "Succesully Deleted"}
