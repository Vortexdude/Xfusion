

class APIError(Exception):
    """All Custom Exception Handles Here"""
    pass

class APIAuthError(APIError):
    """Custom Authentication Error Class"""
    code = 403
    description = "Authentication Error"