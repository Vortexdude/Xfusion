import jwt, datetime


class Jwt:

    @staticmethod
    def encode(data):
        """Generate the Auth token"""
        try:
            payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': data
            }
            return jwt.encode(payload, 'secret', algorithm='HS256')
        except Exception as e:
            return e
        
    @staticmethod
    def decode(token):
        """Decode token from Auth Token"""
        try:
            data = jwt.decode(token, 'secret')
            return data
        except:
            return {'message': 'token is invalid!'}