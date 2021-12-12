"""Flask app configuration."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY') or 'JOB("=jc+9u?#)?d+HVsTE56+9hdq?9UQ9'

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    DB_NAME = "database.db"
    db_url = environ.get("DATABASE_URL") or f"sqlite:///{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
