from model import db, connect_to_db, User, Connection
from datetime import date, datetime


# -------------------- USERS -------------------- #

def create_user(email, username, password, first_name, last_name, img_url, lat, lng, address, city, state):
    """Create and return a new user."""

    user = User(email = email,
                username = username,
                password = password,
                # password = generate_password_hash(password, method='sha256'),
                first_name = first_name,
                last_name = last_name,
                img_url = img_url, 
                lat = lat,
                lng = lng,
                address = address,
                city = city, 
                state = state)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():
    """Return all users."""

    return User.query.all()


def get_user_by_email(email):
    """Find a user by their email address."""

    return User.query.filter(User.email == email).first()


def get_user_by_username(username):
    """Return user given their username"""

    return User.query.filter(User.username == username).first() 


def get_user_by_id(user_id):
    """Return user given their ID"""

    return User.query.filter(User.user_id == user_id).first() 


# -------------------- CONNECTIONS -------------------- #

def create_connection(user_id_1, user_id_2, connected=True):
    """Creates new Connection"""

    connect_date = datetime.today()
    connection = Connection(user_id_1 = user_id_1, 
                            user_id_2 = user_id_2, 
                            connect_date = connect_date, 
                            connected = connected)

    db.session.add(connection)
    db.session.commit()

    return connection


def get_all_connections():
    """Return all Connections."""

    return Connection.query.order_by(Connection.connect_id).all()


def get_connect_by_id(connect_id):
    """Return Connection given its ID"""

    return Connection.query.filter(Connection.connect_id == connect_id).first() 


def get_connect_by_user_id(user_id):
    """Return Connection given its ID"""

    return Connection.query.filter(Connection.user_id == user_id).all() 
