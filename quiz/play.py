from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from quiz import quiz
from models import Quiz, Cards, User
from __init__ import db


# play page
@quiz.route('/play/<quiz_id>/', methods=['GET', 'POST'])
def play(quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    quiz_ = {
        "title": quiz.title,
        "author": User.query.filter_by(id=quiz.author).first().username,
        "cards": Cards.query.filter_by(quiz_id=quiz.id).all()

    }
    return render_template("play_quiz.html", quiz=quiz_)
