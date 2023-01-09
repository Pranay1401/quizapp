from flask import render_template, request, redirect, url_for
from flask_login import login_user
from . import account as blueprint_account
from ..models import db, User


# Register page
@blueprint_account.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            return redirect(url_for('account.register'))
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('quiz.all_quiz'))

    return render_template("register.html")
