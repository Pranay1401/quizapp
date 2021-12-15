from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from quiz import quiz
from models import Quiz, Cards, User, Scoreboard
from __init__ import db
from sqlalchemy import desc


# play page
@quiz.route('/play/<quiz_id>/', methods=['GET', 'POST'])
def play(quiz_id):
    if request.method == "POST":
        time = request.form.get('time')
        score = request.form.get('score')
        user = current_user.username

        quiz = Quiz.query.filter_by(id=quiz_id).first()
        new_scoreboard = Scoreboard(quiz_id=quiz_id, user_id=current_user.id,
                                    time=time, score=score)
        db.session.add(new_scoreboard)
        db.session.commit()

        return redirect(url_for(f"quiz.scoreboard", quiz_id=quiz_id))

    quiz = Quiz.query.filter_by(id=quiz_id).first()
    quiz_ = {
        "title": quiz.title,
        "author": User.query.filter_by(id=quiz.author).first().username,
        "cards": Cards.query.filter_by(quiz_id=quiz.id).all(),
        "pass": 70

    }
    return render_template("play_quiz.html", quiz=quiz_)


# play page
@quiz.route('/play/', methods=['GET'])
def all_quiz():
    all_quizs = Quiz.query.all()
    return render_template("all_quiz.html", all_quizs=all_quizs)


# Scoreboard page
@quiz.route('/scoreboard/<quiz_id>', methods=['GET'])
def scoreboard(quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    scoreboard_all = Scoreboard.query.order_by(Scoreboard.score.desc()).order_by(Scoreboard.time).filter_by(quiz_id=quiz.id).all()
    print(scoreboard_all)
    all_quizzes = []
    for i in range(len(scoreboard_all)):
        quiz_ = {
            "username": User.query.filter_by(id=scoreboard_all[i].user_id).first().username,
            "score": scoreboard_all[i].score,
            "time": scoreboard_all[i].time

        }
        all_quizzes.append(quiz_)
    print(all_quizzes)
    return render_template("play_results.html", quiz=all_quizzes)
