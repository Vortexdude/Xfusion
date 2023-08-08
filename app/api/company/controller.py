from .model import CompanyModel

class CompanyController():
    companies = []

    @classmethod
    def fetch_company(cls):
        _companies = []
        companies = CompanyModel.query.all()
        for company in companies:
            _companies.append({
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
        return {"compnies": _companies}
    
    @classmethod
    def store_company(cls, company_data, loggedInUser):
        _data = {"create_by": loggedInUser, **company_data}
        response = CompanyModel.register_record(_data)
        message = "Record Inserted successfully" if response else "The company already exist on the database"
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
