from flask_login import UserMixin

from __init__ import db


# Quiz object
class Quiz(db.Model, UserMixin):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    cards = db.relationship('Cards', backref='quiz')
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, author):
        self.title = title
        self.author = author


# Options object
class Cards(db.Model, UserMixin):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    question = db.Column(db.String(32), nullable=False)
    correct = db.Column(db.String(32), nullable=False)
    false1 = db.Column(db.String(32), nullable=False)
    false2 = db.Column(db.String(32), nullable=True, default=None)
    false3 = db.Column(db.String(32), nullable=True, default=None)

    def __init__(self, quiz_id, question, correct, false1, false2, false3):
        self.quiz_id = quiz_id
        self.question = question
        self.correct = correct
        self.false1 = false1
        self.false2 = false2
        self.false3 = false3
