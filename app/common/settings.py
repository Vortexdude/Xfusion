import os, subprocess, sys
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
        POSTGRES = {
            "user": self._get_env("POSTGRES_USER", None),
            "pw": self._get_env("POSTGRES_PASSWORD", None),
            "host": self._get_env("POSTGRES_HOST", None),
            "port": self._get_env("POSTGRES_PORT", None),
            "db": self._get_env("POSTGRES_DB", None),
        }
        if not POSTGRES['user']:
            return self._get_env("SQLALCHEMY_DATABASE_URI", "sqlite:///data.db")
        return ("postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES)

    @property
    def sqlalchemy_track_modificatios(self):
        return self._get_env("SQLALCHEMY_TRACK_MODIFICATION", False)

    @property
    def propagate_exception(self):
        return self._get_env("PROPAGATE_EXCEPTIONS", True)

    @property
    def jwt_blacklist_enabled(self):
        return self._get_env("JWT_BLACKLIST_ENABLED", True)
    
    @property
    def jwt_blacklist_tokens(self):
        return self._get_env("JWT_BLACKLIST_TOKEN_CHECKS", True)
    
    @property
    def api_spec_option(self):
        data = {}
        data['security'] = [{"bearerAuth": []}]
        data['components'] = {
                "securitySchemes":
                    {
                        "bearerAuth": {
                            "type":"http",
                            "scheme": "bearer",
                            "bearerFormat": "JWT"
                        }
                    }
            }
        return data

    @property
    def web_port(self):
        return self._get_env("WEB_PORT", 5000)

    @property
    def web_app_name(self):
        return self._get_env("WEB_APP_NAME", "Xfusion")

    @property
    def host(self):
        return self._get_env("HOST", "0.0.0.0")


def run_gunicorn(env):
    command = [
        "gunicorn",
        "-c", "conf/gunicorn.py",
        "--log-config", "conf/gunicorn_log.conf",
        f"app.app:create_app('{env}')",
        "--reload"
    ]
    try:
        subprocess.run(command)
    except KeyboardInterrupt:
        print("\nReceived Ctrl+C. Stopping the server gracefully.")
        sys.exit(0)
