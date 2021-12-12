from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from auth import account
from models import User
from __init__ import db


# login page
@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            return redirect(url_for('account.login'))
        else:
            if user.check_password(password):
                login_user(user, remember=True)
                return "Successfully authenticated"
            else: return redirect(url_for('account.login'))

    return render_template("login.html")
