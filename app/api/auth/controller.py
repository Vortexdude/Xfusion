from app.api.user.model import UserModel
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import request
import datetime, re

MISSING_HEADER = "timeout headers is missing from the header"
UNRECOGNISE_HEADER = "Timeout header containes string character"
WRONG_CREDENTIALS = "You have entred Wrong Credentials"
LOGGED_OUT = "Logged out!"

class HeaderValidator:
    def __init__(self, header):
        self.header = header

    @classmethod
    def timer(cls, header):
        if not header:
            return (False, MISSING_HEADER)
        elif re.search('[a-zA-Z]', header):
            return (False, UNRECOGNISE_HEADER)
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
        data = UserModel.auth(logindata['email'], logindata['password'])
        if not data:
            return {"Message": WRONG_CREDENTIALS}

        payload_data.update({"fname": data.fname, "email": data.email})
        expires = datetime.timedelta(seconds=int(timeout))
        token = create_access_token(identity=payload_data, expires_delta=expires)
        return {"token": str(token), "expired in": timeout}
    
    @staticmethod
    def logout():
        tokendata = get_jwt_identity()
        return {"user": tokendata['fname'], "status": LOGGED_OUT}
    