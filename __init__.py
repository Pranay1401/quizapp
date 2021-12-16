from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from models import Quiz, User
        from auth import account
        from quiz import quiz

        # Register Blueprints
        app.register_blueprint(account, url_prefix='/account/')
        app.register_blueprint(quiz, url_prefix='/quiz/')

        # Create Database Models
        db.create_all()

        @login_manager.user_loader
        def load_user(identifier):
            return User.query.get(int(identifier))

        # Error Management
        @app.errorhandler(404)
        def page_not_found(error):
            return redirect(url_for('quiz.all_quiz'))

        return app
