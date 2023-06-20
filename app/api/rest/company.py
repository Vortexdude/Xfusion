from flask_smorest import Blueprint
from flask.views import MethodView
from app.common.controller.companies import CompanyController


blp = Blueprint("Companies", __name__, description="Get all the companies")

@blp.route("/companies")
class CompanyClass(MethodView):

    def get(self):
        return CompanyController.fetch_company()
    
    def post(self):
        return CompanyController.store_company()
    
    def put(self):
        return CompanyController.update_company()
    
    def delete(self):
        return CompanyController.delete_company()
    