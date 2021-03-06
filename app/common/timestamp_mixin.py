from datetime import datetime
from app.db import db, BaseModelMixin


class TimestampMixin(object):
    created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
