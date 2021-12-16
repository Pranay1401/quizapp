from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from quiz import quiz
from models import Quiz, Cards
from __init__ import db


# login page
@quiz.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        if current_user.is_authenticated:
            user_id = current_user.id
        else:
            user_id = 0
        title = request.form.get(f'title')
        new_quiz = Quiz(title=title, author=user_id)

        for i in range(100):
            question = request.form.get(f'question_{i+1}')
            if not question: break
            correct = request.form.get(f'correct_{i+1}')
            option1 = request.form.get(f'option1_{i+1}')
            option2 = request.form.get(f'option2_{i+1}')
            option3 = request.form.get(f'option3_{i+1}')

            if correct and option1:

                new_quiz.cards.append(Cards(quiz_id=new_quiz.id, question=question, correct=correct,
                                            false1=option1, false2=option2, false3=option3))

        db.session.add(new_quiz)
        db.session.commit()
    return render_template("create_quiz.html")
