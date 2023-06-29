from app.api.user.model import UserModel
from flask_jwt_extended import create_access_token, get_jwt_identity

class AuthController:

    @staticmethod
    def login(logindata):
        payload_data = {}
        data = UserModel.query.filter(UserModel.email == logindata['email']).filter(UserModel.password == logindata['password']).first()
        try:
            if not data.fname:
                pass
        except AttributeError:
                return {"Message": "You have entred Wrong Credentials"}
        payload_data.update({"fname": data.fname, "email": data.email})
        token = create_access_token(identity=payload_data)
        return {"token": str(token), "expired in": 900}
    
    @staticmethod
    def logout():
        tokendata = get_jwt_identity()

        return {"user": tokendata['fname'], "status": "Logged out!"}
    