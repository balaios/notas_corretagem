from datetime import datetime

from ..extensions import db


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    data = db.Column(db.DateTime, default=datetime.utcnow)
