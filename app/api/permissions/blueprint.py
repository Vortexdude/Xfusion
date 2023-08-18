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
        """Fetch all the roles that are present in the database 
        with the help of model method

        Returns:
            json: a list of roles attributes if found
        """     
        return PermController.fetch_roles()

    @jwt_required()
    @blp.arguments(RollSchema)
    def post(self, roledata):
        """To create a new role inside the database using post request
            it will check the name in the database to verify the role is
            exist or not if not then it will create

        Args:
            roledata (json): a list of attributes that need to be set on the database

        Returns:
            json: returns the id of newly create role other wise return the message 
            that role is laready present in the database
        """
        return PermController.create_role(roledata)

    @jwt_required()
    @blp.arguments(UpdateSchema)
    def put(self, roledata):
        """For updating the roles values, that required a identification key or ID 
        so that it will find and update the details in the database

        Args:
            roledata (json): data that need to be updated 

        Returns:
            json: success if id exist in the database
        """
        return PermController.update_role(roledata)

    @jwt_required()
    @blp.arguments(DeleteSchema)
    def delete(self, roledata):
        """for dete the role from the databse it required a id that should be 
        present on the database

        Args:
            roledata (json): key of the role that should be present on the database

        Returns:
            json: message of success and error
        """
        return PermController.delete_role(roledata)

