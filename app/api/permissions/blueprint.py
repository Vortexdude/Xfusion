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
    def post(self, rolldata):
        return PermController.create_role(rolldata)

    @jwt_required()
    @blp.arguments(UpdateSchema)
    def put(self, rolldata):
        return PermController.update_role(rolldata)

    @jwt_required()
    @blp.arguments(DeleteSchema)
    def delete(self, rolldata):
        return PermController.delete_role(rolldata)
