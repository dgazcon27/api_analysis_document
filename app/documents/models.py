from app.db import db, BaseModelMixin
from app.common.timestamp_mixin import TimestampMixin


class Documents(db.Model, BaseModelMixin, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_by_title(self):
        return Documents.query.filter_by(name=self.name).first()
