from flask import Flask, request
from flask_smorest import Api
from db import db
from resources import UserBluePrint, AuthBlueprint
import os
#factory Structure
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Xfusion Rest API"
    app.config["API_VERSION"] = "1.0"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(UserBluePrint)

    return app
