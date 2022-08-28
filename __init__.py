from os import environ

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

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
        from models import User
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

        quest = User.query.filter_by(id=0).first()
        if not quest:
            # Quest user will be added to scoreboard when user is not signed in
            new_user = User(id=0, username="Guest")
            new_user.set_password(environ.get("QUEST_PASSWORD") or "Pa$$w0rd")
            db.session.add(new_user)
            db.session.commit()
            print("Quest user created")

        return app
