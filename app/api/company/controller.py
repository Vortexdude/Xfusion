from .model import CompanyModel
from sqlalchemy.exc import SQLAlchemyError
from conf.config_const import CONF

class CompanyController():

    @classmethod
    def fetch_company(cls):
        companies = CompanyModel.fetch_all()
        return {"companies": companies}

    @classmethod
    def store_company(cls, company_data, logged_in_user):
        _data = {"create_by": logged_in_user, **company_data}
        company = CompanyModel(**_data)

        try:
            company.save_to_db()
            return {"company_id": company.to_json()['id']}
        except SQLAlchemyError as e:
            if "UNIQUE constraint" in str(e):
                return {"message": CONF['company_already_exist']}
            else:
                return {"message": CONF['database_error']}

    @classmethod
    def update_company(cls, company_data, logged_in_user, id):
        company = CompanyModel.fetch_record_by_id(id=id)
        if not company:
            return {"message": CONF['wrong_key']}

        response = CompanyModel.update_record(logged_in_user=logged_in_user, id=id, **company_data)
        return {"message": CONF['data_updated']} if response else {"message": CONF['key_not_found']}

    @classmethod
    def delete_company(cls, key):
        company = CompanyModel.fetch_record_by_id(id=key)
        
        if not company:
            return {"message": CONF['key_not_found']}

        try:
            company.delete_from_db()
            return {"message": CONF['company_deleted']}
        except SQLAlchemyError:
            return {"message": CONF['database_error']}
