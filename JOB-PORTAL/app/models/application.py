from datetime import datetime
from app.extensions.db import db

class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Ensure a user can only apply to a specific job once
    __table_args__ = (db.UniqueConstraint('user_id', 'job_id', name='unique_application'),)