from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from . import account as blueprint_account
from ..models import User


# login page
@blueprint_account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user:
            return redirect(url_for('account.login'))
        else:
            if user.check_password(password):
                login_user(user, remember=True)
                return redirect(url_for('quiz.all_quiz'))
            else:
                return redirect(url_for('account.login'))

    return render_template("login.html")


# login page
@login_required
@blueprint_account.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('quiz.all_quiz'))
