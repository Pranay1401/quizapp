from flask_login import UserMixin

from . import db


# Quiz object
class Quiz(db.Model, UserMixin):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    cards = db.relationship('Cards', backref='quiz')
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    best_time = db.Column(db.Integer, nullable=False, default=0)
    total_tries = db.Column(db.Integer, nullable=False, default=0)
    scoreboard = db.relationship('Scoreboard', backref='quiz')

    def __init__(self, title, author):
        self.title = title
        self.author = author


# Cards object
class Cards(db.Model, UserMixin):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    question = db.Column(db.String(128), nullable=False)
    correct = db.Column(db.String(64), nullable=False)
    false1 = db.Column(db.String(64), nullable=False)
    false2 = db.Column(db.String(64), nullable=True, default=None)
    false3 = db.Column(db.String(64), nullable=True, default=None)

    def __init__(self, quiz_id, question, correct, false1, false2, false3):
        self.quiz_id = quiz_id
        self.question = question
        self.correct = correct
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3


# Scoreboard object
class Scoreboard(db.Model, UserMixin):
    __tablename__ = 'scoreboard'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, quiz_id, user_id, time, score):
        self.quiz_id = quiz_id
        self.user_id = user_id
        self.time = time
        self.score = score
