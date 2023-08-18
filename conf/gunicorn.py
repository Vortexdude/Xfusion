from app.common import settings

bind = f"{settings.host}:{settings.web_port}"
workers = 2
