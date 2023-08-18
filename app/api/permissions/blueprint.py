from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from .controller import PermController
from .schema import RollSchema, UpdateSchema, DeleteSchema

blp = Blueprint("Permission/roles", __name__, description="Permision and roles related operations")

@blp.route("/roles")
class Roles(MethodView):

    @jwt_required()
    def get(self):
        return PermController.fetch_roles()

    @jwt_required()
    @blp.arguments(RollSchema)
    def post(self, roledata):
        return PermController.create_role(roledata)

    @jwt_required()
    @blp.arguments(UpdateSchema)
    def put(self, roledata):
        return PermController.update_role(roledata)

    @jwt_required()
    @blp.arguments(DeleteSchema)
    def delete(self, roledata):
        return PermController.delete_role(roledata)

