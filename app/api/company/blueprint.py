from flask_smorest import Blueprint
from flask.views import MethodView
from .controller import CompanyController
from .schema import CompanySchema, CompanyUpdateSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

blp = Blueprint("Companies", __name__, description="Get all the companies")

@blp.route("/companies")
class CompanyClass(MethodView):
    
    @jwt_required()
    def __init__(self):
        self.user = get_jwt_identity()
        self.logged_in_user = self.user['fname']

    @jwt_required()
    def get(self):
        """For get all the companies data with the get method

        Returns:
            json: list of companies details
        """
        return CompanyController.fetch_company()

    @jwt_required()
    @blp.arguments(CompanySchema)
    def post(self, company_data):
        """For creating a new company that required a json body

        Args:
            company_data (json): need to provide the data for company, id will not required 
            it will created automatically by self

        Returns:
            json: message: succesfully Registerd the company
        """
        return CompanyController.store_company(company_data, self.logged_in_user)

@blp.route("/company/<string:company_id>")
class CompanyOpeations(MethodView):

    def __init__(self):
        CompanyClass.__init__(self)
    
    @jwt_required()
    def delete(self, company_id):
        """For deleting the comapny record from the database

        Args:
            key (id): identification details of the registered comapny

        Returns:
            json: message -> company delete succesfully!
        """
        return CompanyController.delete_company(company_id)
    
    @jwt_required()
    @blp.arguments(CompanyUpdateSchema)
    def put(self, company_data, company_id):
        """For updating the company details you need to give the identification details

        Args:
            company_data (json): identification details uuid

        Returns:
            json: message
        """ 
        return CompanyController.update_company(company_data, logged_in_user=self.logged_in_user, id=company_id)
