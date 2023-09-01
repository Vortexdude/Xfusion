from functools import wraps
from flask import request
from datetime import datetime
from .model import LogModel


class logging:
    def __init__(self, mode: str = "info") -> None:
        self.mode = mode.upper()
        self.stringformat = "{timestamp} {mode} {remote_addr} -> {action} {data}"
        self.source = "file"

    def config(self, source: str = None, stringformat: str = None) -> None:
        if source:
            self.source = source
        if stringformat:
            self.stringformat = stringformat

    def log_audit_trail(self, action):
        def decorator(function):
            @wraps(function)
            def wrapper(*args, **kwargs):
                timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                email = request.get_json()['email']
                remote_addr = request.remote_addr
                string = self.stringformat.format(timestamp=timestamp, data=email, mode=self.mode, action=action, remote_addr=remote_addr)
                # string = f"[{timestamp}] {mode.upper()} -- {remote_addr} -> {action} {email}"
                # print(string)
                if self.source == 'model':
                    data = LogModel(timestamp, self.mode, email, remote_addr)
                    data.save_to_db()
                    print(data.to_json())
                return function(*args, **kwargs)
            return wrapper
        return decorator
