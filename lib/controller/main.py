from lib.models import UserModel
from resources.auth.jwt import Jwt

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
        token = Jwt.encode({"name": payload_data})
        return {"token": str(token), **payload_data}
    
    @staticmethod
    def logout():
        return {"Message": "You are logout Succesfull"}
    