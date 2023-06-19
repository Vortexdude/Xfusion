################################
# ------ AIM          --> Factory Structure for Flask api 
# ------ Developed by --> Nitin Namdev -------------------
# ------ API Documentation --> Swagger -------------------
# ------ Views --> Flask_views and Methodview -------------
# ------ Database --> SQLITE3 ----------------------------
# ------ ORM --> SQLAlchemy ------------------------------
# ------ Model --> Marshmellow ---------------------------

################################

from flask import Flask, request
from flask_smorest import Api
from db import db
from resources import UserBluePrint, AuthBlueprint
import os
from config import devconf

#factory Structure
def create_app(db_url=None):
    app = Flask(__name__)
    app.config.update(**devconf)
    api = Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    #registeting the routes named as blueprint
    api.register_blueprint(AuthBlueprint)
    api.register_blueprint(UserBluePrint)

    return app
