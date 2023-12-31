from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from .controller import PermController
from .schema import RoleSchema, UpdateSchema

blp = Blueprint("Permission/roles", __name__, description="Permision and roles related operations")

@blp.route("/roles")
class Roles(MethodView):

    @jwt_required()
    def __init__(self):
        self.user = get_jwt_identity()
        self.loggedInUser = self.user['fname']

    @jwt_required()
    def get(self) -> dict:
        """Fetch all the roles that are present in the database 
        with the help of model method

        Returns:
            json: a list of roles attributes if found
        """     
        return PermController.fetch_roles()

    @jwt_required()
    @blp.arguments(RoleSchema)
    def post(self, roledata: dict) -> dict:
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


@blp.route("/role/<string:role_id>")
class RoleEditor(MethodView):

    def __init__(self):
        Roles.__init__(self)

    def get(self, role_id:str) -> dict:
        """For get the role details via RoleID 
        so that it will find the details in the database

        Args:
            id (string): id of the role that should exist on the database

        Returns:
            json: success if id exist in the database
        """        
        return PermController.get_role(role_id)

    @jwt_required()
    @blp.arguments(UpdateSchema)
    def put(self, roledata: dict, role_id: str) -> dict:
        """For updating the roles values, that required a identification key or ID 
        so that it will find and update the details in the database

        Args:
            roledata (json): data that need to be updated 

        Returns:
            json: success if id exist in the database
        """
        return PermController.update_role(roledata, role_id)

    @jwt_required()
    def delete(self, role_id: str) -> dict:
        """for dete the role from the databse it required a id that should be 
        present on the database

        Args:
            roledata (json): key of the role that should be present on the database

        Returns:
            json: message of success and error
        """
        return PermController.delete_role(role_id)
