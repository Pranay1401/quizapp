from flask import Blueprint

quiz = Blueprint('quiz', __name__)

from .create import create
from .play import play
# from .logout import logout
