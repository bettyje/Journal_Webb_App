from datetime import datetime
from extensions import db
import bcrypt

# User Model


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    theme = db.Column(db.String(10), default="light")
    journals = db.relationship(
        'JournalEntry', back_populates='user', cascade="all, delete-orphan")

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(
            password.encode('utf-8'), salt).decode('utf8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Journal Entry Model


class JournalEntry(db.Model):
    __tablename__ = "journal_entry"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='journals')
