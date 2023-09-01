from app.database.db import db
from uuid import uuid4

class LogModel(db.Model):
    __tablename__ = "logging"
    id = db.Column(db.String(255), nullable=True, primary_key=True)
    timestamp = db.Column(db.String, nullable=False)
    mode = db.Column(db.String, nullable=False)
    data = db.Column(db.String, nullable=False)
    remote_addr = db.Column(db.String(50), nullable=False)

    def __init__(self, timestamp, mode, data, remote_addr):
        self.id = str(uuid4())
        self.timestamp = timestamp
        self.mode = mode
        self.data = data
        self.remote_addr = remote_addr

    def to_json(self):
        return {
            "timestamp": self.timestamp,
            "mode": self.mode,
            "data": self.data,
            "remote_addr": self.remote_addr
        }


    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
