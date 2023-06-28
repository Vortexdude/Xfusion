from app.model.company import CompanyModel
from app.database.db import db
from sqlalchemy.exc import SQLAlchemyError
from uuid import uuid4

class CompanyController():
    companies = []

    @classmethod
    def fetch_company(cls):
        cls.companies = []
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
                "location": company.location,
                "create_by": company.create_by,
                "updated_by": company.updated_by

            })
        return {"compnies": cls.companies}
    
    @classmethod
    def fetch_one_company(cls, key):
        company = CompanyModel.query.filter_by(legal_entity_name=key).first()
        return company

    @classmethod
    def store_company(cls, company_data, loggedInUser):
        legal_entity_key = str(uuid4().hex)
        _data = {"legal_entity_key": legal_entity_key, "create_by": loggedInUser, **company_data}
        model_data = CompanyModel(**_data)
        try:
            db.session.add(model_data)
            db.session.commit()
        except SQLAlchemyError as e:
            return {"data": "The company already exist on the database"}    
            
        return {"data": "inserted succesfully !"}

    @classmethod
    def update_company(cls, company_data, loggedInUser):
        company = cls.fetch_one_company(company_data['legal_entity_name'])
        if bool(company):
            if company_data['legal_entity_name']:
                company.legal_entity_name = company_data['legal_entity_name']

            if company_data['account_type']:
                company.account_type = company_data['account_type']

            if company_data['status']:
                company.status = company_data['status']

            if company_data['location']:
                company.location = company_data['location']

            company.updated_by = loggedInUser

            db.session.commit()
            return {"Message": "data updated succesfully"}
        else:
            return {"Message": "Incorrect company Name"}
    
    @classmethod
    def delete_company(cls, key):
        CompanyModel.query.filter_by(legal_entity_key=key['legal_entity_key']).delete()
        db.session.commit()        
        return {"Status": "Succesully Deleted"}
