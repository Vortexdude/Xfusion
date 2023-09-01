from app.api.user.model import UserModel
from app.common.logging import logging
from conf.config_const import CONF
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask import request
import datetime, re

log = logging(mode="warn")
log.config(source='model')

class HeaderValidator:
    def __init__(self, header):
        self.header = header

    @classmethod
    def timer(cls, header: str) -> tuple:
        if not header:
            return (False, CONF['missing_header'])
        elif re.search('[a-zA-Z]', header):
            return (False, CONF['unrecognise_header'])
        else:
            return (True, "")
 
class AuthController:

    @log.log_audit_trail("login")
    @staticmethod
    def login(logindata: dict) -> dict:
        timeout = request.headers.get("timeout")
        message = ""
        if not HeaderValidator.timer(timeout)[0]:
             message = HeaderValidator.timer(timeout)[1]
             return {"message": message}
        payload_data = {}
        data = UserModel.auth(logindata['email'], logindata['password'])
        if not data:
            return {"Message": CONF['wrong_creds']}

        payload_data.update({"fname": data.fname, "email": data.email})
        expires = datetime.timedelta(seconds=int(timeout))
        token = create_access_token(identity=payload_data, expires_delta=expires)
        return {"token": str(token), "expired in": timeout}

    @staticmethod
    def logout() -> dict:
        tokendata = get_jwt_identity()
        return {"user": tokendata['fname'], "status": CONF['logged_out']}
