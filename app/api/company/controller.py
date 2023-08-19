from .model import CompanyModel
from sqlalchemy.exc import SQLAlchemyError
from conf.config_const import CONF

class CompanyController():

    @classmethod
    def fetch_company(cls):
        companies = CompanyModel.fetch_all()
        return {"companies": companies}

    @classmethod
    def store_company(cls, company_data, loggedInUser):
        _data = {"create_by": loggedInUser, **company_data}
        company = CompanyModel(**_data)
        try:
            company.save_to_db()
            message = CONF['company_registerd']
        except SQLAlchemyError as e:
            if "UNIQUE constraint" in str(e):
                message = CONF['company_already_exist']
            else:
                message = CONF['database_error']
        return {"message": message}

    @classmethod
    def update_company(cls, company_data, loggedInUser, id):
        company = CompanyModel.fetch_record_by_id(id=id)
        if not company:
            return {"message": CONF['wrong_key']}

        response = CompanyModel.update_record(loggedInUser=loggedInUser, id=id, **company_data)
        message = CONF['data_updated'] if response else CONF['key_not_found']
        return {"message": message}

    @classmethod
    def delete_company(cls, key):
        company = CompanyModel.fetch_record_by_id(id=key)
        
        if not company:
            return {"message": CONF['key_not_found']}

        try:
            company.delete_from_db()
            message = CONF['company_deleted']
        except SQLAlchemyError:
            message = CONF['database_error']
        
        return {"message": message}