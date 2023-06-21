from app.common import settings

class FlaskConfiguration:

    JWT_SECRET_KEY = settings.jwt_secret_key
    PROPAGATE_EXCEPTIONS = settings.propagate_exception
    API_TITLE = settings.api_title
    API_VERSION = settings.api_version
    OPENAPI_VERSION = settings.openapi_version
    OPENAPI_URL_PREFIX = settings.openapi_url_prefix
    OPENAPI_SWAGGER_UI_PATH = settings.openapi_swagger_ui_path
    OPENAPI_SWAGGER_UI_URL = settings.openapi_swagger_ui_url
    SQLALCHEMY_DATABASE_URI = settings.sqlalchemy_database_uri
    SQLALCHEMY_TRACK_MODIFICATION = settings.sqlalchemy_track_modificatios
    