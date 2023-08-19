from .model import CompanyModel
from sqlalchemy.exc import SQLAlchemyError

COMPANY_REGISTERED_SUCCESSFULLY = "Company registered successfully"
COMPANY_ALREADY_EXIST = "The company already exists in the database"
DATABASE_ERROR = "An error occurred, possibly due to a database issue"
ENTERED_WRONG_KEY = "You have entered the wrong key"
DATA_UPDATED_SUCCESSFULLY = "Data updated successfully"
KEY_NOT_FOUND = "Entered key not found in the database"
WRONG_CREDENTIALS = "You have entered wrong credentials"
COMPANY_DELETED_SUCCESSFULLY = "Company successfully deleted"

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
            message = COMPANY_REGISTERED_SUCCESSFULLY
        except SQLAlchemyError as e:
            if "UNIQUE constraint" in str(e):
                message = COMPANY_ALREADY_EXIST
            else:
                message = DATABASE_ERROR
        return {"message": message}

    @classmethod
    def update_company(cls, company_data, loggedInUser, id):
        company = CompanyModel.fetch_record_by_id(id=id)
        if not company:
            return {"message": ENTERED_WRONG_KEY}

        response = CompanyModel.update_record(loggedInUser=loggedInUser, id=id, **company_data)
        message = DATA_UPDATED_SUCCESSFULLY if response else KEY_NOT_FOUND
        return {"message": message}

    @classmethod
    def delete_company(cls, key):
        company = CompanyModel.fetch_record_by_id(id=key)
        
        if not company:
            return {"message": KEY_NOT_FOUND}

        try:
            company.delete_from_db()
            message = COMPANY_DELETED_SUCCESSFULLY
        except SQLAlchemyError:
            message = DATABASE_ERROR
        
        return {"message": message}