from app.model.company import CompanyModel


class CompanyController():
    companies = []

    @classmethod
    def fetch_company(clas):
        # companies = CompanyModel.query.all()
        # for company in companies:
        #     CompanyController.companies.append({
        #         company
        #     })
        return {"Status": "Worked! from controller Returned"}

    @classmethod
    def store_company(cls):
        return {"Status": "Worked! from controller Stored"}
    
    @classmethod
    def update_company(cls):
        return {"Status": "Worked! from controller Updated"}
    
    @classmethod
    def delete_company(cls):
        return {"Status": "Worked! from controller Deleted"}