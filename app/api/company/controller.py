from .model import CompanyModel

class CompanyController():
    companies = []

    @classmethod
    def fetch_company(cls):
        compnies = CompanyModel.fetch_all()
        return {"compnies": compnies}

    @classmethod
    def store_company(cls, company_data, loggedInUser):
        _data = {"create_by": loggedInUser, **company_data}
        company = CompanyModel(**_data)
        company.save_to_db()
        message = "Record Inserted successfully" if company else "The company already exist on the database"
        return {"message": message}

    @classmethod
    def update_company(cls, company_data, loggedInUser):
        response = CompanyModel.update_record(loggedInUser=loggedInUser, **company_data)
        message = "data updated succesfully" if response else "Key not found"
        return {"message": message}
    
    @classmethod
    def delete_company(cls, key):
        legal_entity_key = key['legal_entity_key']
        if legal_entity_key:
            response = CompanyModel.delete_record(legal_entity_key)
            message= "Company succesully deleted" if response else "Incorrect Id!"
        else:
            message = "legal_entity_key not found"
        return {"message": message}
