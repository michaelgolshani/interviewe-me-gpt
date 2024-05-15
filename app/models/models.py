from datetime import datetime
from .db import db


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    ai_summary = db.Column(db.String(5000), default="", nullable=True)

    def __repr__(self):
        return f'<Appintment {self.id}>'

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "date": self.date,
            "time": self.time,
            "ai_summary": self.ai_summary,
        }

