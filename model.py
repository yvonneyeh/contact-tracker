"""Models for contact tracking app."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """An app user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    img_url = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    address = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(3))
    
    # connections: a list of Connection objects associated with user.
    # connection = db.relationship('Connection')

    def __repr__(self):
        """Show info about user."""

        return f"<User_id: {self.user_id} Name: {self.first_name} {self.last_name}>"


class Connection(db.Model):
    """A connection between 2 Users."""

    __tablename__ = "connections"

    connect_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_1 = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user_2 = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    connect_date = db.Column(db.DateTime)

    U1 = db.relationship('User', foreign_keys=[user_1], backref='connections')
    U2 = db.relationship('User', foreign_keys=[user_2], backref='connections')

    def __repr__(self):
        """Show info about connection."""
        
        return f'<Connection connect_id: {self.connect_id} U1: {self.user_1} U2: {self.user_2}>'


def connect_to_db(flask_app, db_uri='postgresql:///contacts', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to DB!')        



if __name__ == '__main__':
    from app import app
    connect_to_db(app, echo=False)
    db.create_all()