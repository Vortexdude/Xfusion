from app.api.user.model import UserModel
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import request
import datetime, re

class HeaderValidator:
    def __init__(self, header):
        self.header = header

    @classmethod
    def timer(cls, header):
        if not header:
             return (False, "timeout headers is missing from the header")
        elif re.search('[a-zA-Z]', header):
             return (False, "Timeout header containes string character")
        else:
             return (True, "")
 
class AuthController:

    @staticmethod
    def login(logindata):
        timeout = request.headers.get("timeout")
        message = ""
        if not HeaderValidator.timer(timeout)[0]:
             message = HeaderValidator.timer(timeout)[1]
             return {"message": message}
        payload_data = {}
        data = UserModel.query.filter(UserModel.email == logindata['email']).filter(UserModel.password == logindata['password']).first()
        try:
            if not data.fname:
                pass
        except AttributeError:
                return {"Message": "You have entred Wrong Credentials"}
        payload_data.update({"fname": data.fname, "email": data.email})
        expires = datetime.timedelta(seconds=int(timeout))
        token = create_access_token(identity=payload_data, expires_delta=expires)
        return {"token": str(token), "expired in": timeout}
    
    @staticmethod
    def logout():
        tokendata = get_jwt_identity()

        return {"user": tokendata['fname'], "status": "Logged out!"}
    