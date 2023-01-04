from flask import Flask, redirect, url_for
from flask_login import LoginManager
from .models import db


login_manager = LoginManager()

app = Flask(__name__)

# Application Configuration
app.config.from_object("project.config.Config")

# Initialize Plugins
db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    from .models import User

    from .quiz import quiz
    from .auth import account

    # Register Blueprints
    app.register_blueprint(account, url_prefix='/account/')
    app.register_blueprint(quiz, url_prefix='/quiz/')

    @login_manager.user_loader
    def load_user(identifier):
        return User.query.get(int(identifier))

    # Error Management
    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('quiz.all_quiz'))
