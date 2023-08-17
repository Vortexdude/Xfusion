from flask_smorest import Blueprint
from flask.views import MethodView
from .controller import CompanyController
from .schema import CompanySchema, CompanyDelSchema, CompanyUpdateSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

blp = Blueprint("Companies", __name__, description="Get all the companies")

@blp.route("/companies")
class CompanyClass(MethodView):
    
    @jwt_required()
    def __init__(self):
        self.user = get_jwt_identity()
        self.loggedInUser = self.user['fname']

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
        return CompanyController.store_company(company_data, self.loggedInUser)

    @jwt_required()
    @blp.arguments(CompanyUpdateSchema)
    def put(self, company_data):
        """For updating the company details you need to give the identification details

        Args:
            company_data (json): identification details uuid

        Returns:
            json: message
        """ 
        return CompanyController.update_company(company_data, loggedInUser=self.loggedInUser)

    @jwt_required()
    @blp.arguments(CompanyDelSchema)
    def delete(self, key):
        """For deleting the comapny record from the database

        Args:
            key (id): identification details of the registered comapny

        Returns:
            json: message -> company delete succesfully!
        """
        return CompanyController.delete_company(key)
    