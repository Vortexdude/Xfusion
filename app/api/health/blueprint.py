from flask.views import MethodView
from flask_smorest import Blueprint
from .controller import ServerMonitor

blp = Blueprint("health", __name__, description="Get the health of the system")

@blp.route("/health")
class HealthMonitor(MethodView):
    def get(self):
        return ServerMonitor.get()
