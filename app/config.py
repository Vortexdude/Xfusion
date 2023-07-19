import os
from app.common import settings

basedir = os.path.abspath(os.path.dirname(__file__))

class DefaultConfiguration:
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
    JWT_BLACKLIST_ENABLED = settings.jwt_blacklist_enabled
    JWT_BLACKLIST_TOKEN_CHECKS = settings.jwt_blacklist_tokens
    API_SPEC_OPTIONS = settings.api_spec_option


class DevelopmentConfig(DefaultConfiguration):
    """For Development Environment"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(DefaultConfiguration):
    """For Testing Environment"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(DefaultConfiguration):
    """For Production Environment"""

    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
