import os
from typing import Any
from dotenv import load_dotenv

class Settings:

    def __init__(self):
        load_dotenv(verbose=True)

    @staticmethod
    def _get_env(key, default):
        return os.getenv(key, default)

    @property
    def jwt_secret_key(self):
        return self._get_env("JWT_SECRET_KEY", "secret")

    @property
    def api_title(self):
        return self._get_env("API_TITLE", "Xfusion Rest API")

    @property
    def api_version(self):
        return self._get_env("API_VERSION", "1.0")

    @property
    def openapi_version(self):
        return self._get_env("OPENAPI_VERSION", "3.0.3")

    @property
    def openapi_url_prefix(self):
        return self._get_env("OPENAPI_URL_PREFIX", "/")

    @property
    def openapi_swagger_ui_path(self):
        return self._get_env("OPENAPI_SWAGGER_UI_PATH", "/swagger-ui")

    @property
    def openapi_swagger_ui_url(self):
        return self._get_env("OPENAPI_SWAGGER_UI_URL", "https://cdn.jsdelivr.net/npm/swagger-ui-dist/")

    @property
    def sqlalchemy_database_uri(self):
        return self._get_env("SQLALCHEMY_DATABASE_URI", "sqlite:///data.db")

    @property
    def sqlalchemy_track_modificatios(self):
        return self._get_env("SQLALCHEMY_TRACK_MODIFICATION", False)

    @property
    def propagate_exception(self):
        return self._get_env("PROPAGATE_EXCEPTIONS", True)
