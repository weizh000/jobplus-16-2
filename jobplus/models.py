from datetime import datetime
from flask_sqlalchemy import SQLALhemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLALchemy()

class Base(db.Model):
    __abstract__ True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
            default=datetime.utnow,
            onupdate=datetime.utnow)

user_job = db.Table(
        'user_job',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
        db.Column('job_id', db.Integer, db.ForeignKey('job.id', ondelete='CASCADE'))
)

class User(Base, UserMixin):
    __tablename__ = 'user'

    ROLE_USER = 10
    ROLE_COMANY = 20
    ROLE_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    resume = db.relationship('Resume', uselist=False)
    collect_jobs = db.relationship('Job', secondary=user_job)
    upload_resume_url = db.Column(db.String(64))

    def __repr__(self):
        return '<User:{}'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, orig_password):
        return check_password_hash(self._password, password)




