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
from app.api.user import UserBluePrint
from app.api.auth import AuthBluePrint
from app.api.company import CompanyBluePrint
from app.api.dcim import DcimBluePrint
from app.api.permissions import PermBlueprint
from app.api.health import HealthBlueprint
# from app.api.image_proccessing import ImageProccessingBlueprint
from flask_jwt_extended import JWTManager
from app.config import config_by_name
from conf.config_const import BANNER

def create_app(env: str = "dev"):
    """App Starts form there"""

    app = Flask(__name__)
    app.logger.info(BANNER)
    app.logger.info(f"Using Environment - {env}")
    app.config.from_object(config_by_name[env])
    app.logger.info(f"Using the database - {config_by_name[env].__dict__['SQLALCHEMY_DATABASE_URI'].split(':')[0]}")
    register_extensions(app)
    app.logger.info("Registering extentions...")
    register_blueprints(app)
    app.logger.info("Registering Blueprint...")
    return app

def register_extensions(app) -> None:
    """Registrating the extions"""

    global api
    JWTManager(app)
    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

def register_blueprints(app) -> None:
    """Registration of blueprints"""

    api.register_blueprint(AuthBluePrint)
    api.register_blueprint(UserBluePrint)
    api.register_blueprint(DcimBluePrint)
    api.register_blueprint(CompanyBluePrint)
    api.register_blueprint(PermBlueprint)
    api.register_blueprint(HealthBlueprint)
    # api.register_blueprint(ImageProccessingBlueprint)
