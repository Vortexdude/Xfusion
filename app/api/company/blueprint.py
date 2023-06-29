from flask_smorest import Blueprint
from flask.views import MethodView
from .controller import CompanyController
from .schema import CompanySchema, CompanyDelSchema
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
        return CompanyController.fetch_company()

    @jwt_required()
    @blp.arguments(CompanySchema)
    def post(self, company_data):
        return CompanyController.store_company(company_data, self.loggedInUser)

    @jwt_required()
    @blp.arguments(CompanySchema)
    def put(self, company_data):
        return CompanyController.update_company(company_data, self.loggedInUser)

    @jwt_required()
    @blp.arguments(CompanyDelSchema)
    def delete(self, key):
        return CompanyController.delete_company(key)
    