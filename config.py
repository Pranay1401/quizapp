"""Flask app configuration."""
from os import environ, path


basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_DEBUG') or True
    SECRET_KEY = environ.get('SECRET_KEY') or 'Km&zT!1@a#F1H^y1KEYtNGuR##pR4NPy'

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI: str = environ.get('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
