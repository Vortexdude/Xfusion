################################
# ------ AIM          --> Factory Structure for Flask api 
# ------ Developed by --> Nitin Namdev -------------------
# ------ API Documentation --> Swagger -------------------
# ------ Views --> Flask_views and Methodview -------------
# ------ Database --> SQLITE3 ----------------------------
# ------ ORM --> SQLAlchemy ------------------------------
# ------ Model --> Marshmellow ---------------------------
################################

from flask import Flask
from flask_smorest import Api
from app.database.db import db
from app.api.rest import UserBluePrint, DcimBluePrint, AuthBluePrint, CompanyBluePrint
from flask_jwt_extended import JWTManager
from app.config import FlaskConfiguration

def create_app(db_url=None):
    """App Starts form there"""

    app = Flask(__name__)
    register_extensions(app)
    register_blueprints(app)
    return app

def register_extensions(app):
    """Registrating the extions"""

    app.config.from_object(FlaskConfiguration)
    global api
    JWTManager(app)
    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_blueprints(app):
    """Registration of blueprints"""

    api.register_blueprint(AuthBluePrint)
    api.register_blueprint(UserBluePrint)
    api.register_blueprint(DcimBluePrint)
    api.register_blueprint(CompanyBluePrint)
