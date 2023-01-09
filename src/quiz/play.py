import random
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from ..models import Scoreboard, db, Quiz, User, Cards
from . import quiz as blueprint_quiz


# play page
@blueprint_quiz.route('/play/<quiz_id>', methods=['GET', 'POST'])
def play(quiz_id):
    if current_user.is_authenticated:
        user_id = current_user.id
    else:
        user_id = 0
    if request.method == "POST":
        time = request.form.get('time')
        score = request.form.get('score')

        new_scoreboard = Scoreboard(quiz_id=quiz_id, user_id=user_id,
                                    time=time, score=score)
        db.session.add(new_scoreboard)
        db.session.commit()

        return redirect(url_for('quiz.scoreboard', quiz_id=quiz_id))

    quiz = Quiz.query.filter_by(id=quiz_id).first()
    all_cards = Cards.query.filter_by(quiz_id=quiz.id).all()
    randoms = []
    for i in range(len(all_cards)):
        if all_cards[i].false3:
            length = 4
        elif all_cards[i].false2:
            length = 3
        elif all_cards[i].false1:
            length = 2
        else:
            print('error line 43')
            length = 0
        x = random.randint(0, length - 1)
        randoms.append(x)

    quiz_ = {
        "title": quiz.title,
        "author": User.query.filter_by(id=quiz.author).first().username,
        "cards": all_cards,
        "pass": 70,
        "randoms": randoms

    }
    return render_template("play_quiz.html", quiz=quiz_)


# play page
@blueprint_quiz.route('/play', methods=['GET'])
def all_quiz():
    all_quizs = Quiz.query.all()
    total_takes = []
    best_times = []
    for i in range(len(all_quizs)):
        try:
            total_take = len(Scoreboard.query.filter_by(quiz_id=i + 1).all())
            best_time = Scoreboard.query.order_by(Scoreboard.score.desc()).order_by(Scoreboard.time).filter_by(
                quiz_id=i + 1).first().time
        except AttributeError:
            best_time = "None"
            total_take = "None"
        best_times.append(best_time)
        total_takes.append(total_take)
    return render_template("all_quiz.html", all_quizs=all_quizs, best_times=best_times, total_takes=total_takes)


# Scoreboard page
@blueprint_quiz.route('/scoreboard/<quiz_id>', methods=['GET'])
def scoreboard(quiz_id):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if quiz:
        scoreboard_all = Scoreboard.query.order_by(Scoreboard.score.desc()).order_by(Scoreboard.time).filter_by(
            quiz_id=quiz.id).all()
        all_quizzes = []
        for i in range(len(scoreboard_all)):
            quiz_ = {
                "username": User.query.filter_by(id=scoreboard_all[i].user_id).first().username,
                "score": scoreboard_all[i].score,
                "time": scoreboard_all[i].time

            }
            all_quizzes.append(quiz_)
        return render_template("play_results.html", quiz=all_quizzes)
    return redirect(url_for("quiz.all_quiz"))
