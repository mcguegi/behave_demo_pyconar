from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def drop_all():
    """
    Drop all tables in DB
    :return:
    """
    db.drop_all()


def create_all():
    """
    Create all tables in DB
    :return:
    """
    db.create_all()


def remove_session():
    """
    Removes DB Session
    :return:
    """
    db.session.remove()
