from flask_smorest import Blueprint
from flask.views import MethodView
from app.common.controller.companies import CompanyController
from app.api.schema.company import CompanySchema, CompanyDelSchema

blp = Blueprint("Companies", __name__, description="Get all the companies")

@blp.route("/companies")
class CompanyClass(MethodView):

    def get(self):
        return CompanyController.fetch_company()

    @blp.arguments(CompanySchema)
    def post(self, company_data):
        return CompanyController.store_company(company_data)

    @blp.arguments(CompanySchema)
    def put(self, company_data):
        return CompanyController.update_company(company_data)

    @blp.arguments(CompanyDelSchema)
    def delete(self, key):
        return CompanyController.delete_company(key)
    