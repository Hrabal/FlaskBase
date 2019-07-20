# -*- coding: utf-8 -*-
from flask import g
from flask_login import current_user, login_user, logout_user, login_required

from app import app, login_manager
from models.user import User

TEMP_USER_FORM = """
<form class="form" action="/login" method="post">
    {error}
    <input type="text" name="username" required/>
        <label for="username">Username</label>
    <input type="password" name="password" required/>
        <label for="password">Password</label>
    <input type="hidden" name="referrer" value="{referrer}"/>
    <button type="submit">Login</button>
</form>
"""


@app.before_request
def before_request():
    g.user = current_user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user:
            form_password = request.form["password"].encode("utf-8")
            if bcrypt.checkpw(form_password, user.password):
                login_user(user, remember=True)
                return redirect(request.form["referrer"])
            else:
                login_page.set_form(request.form)
                return TEMP_USER_FORM.format(
                    referrer=request.referrer, error="Wrong Password"
                )
        else:
            return TEMP_USER_FORM.format(
                referrer=request.referrer, error="Wrong Username"
            )
    return TEMP_USER_FORM.format(referrer=request.referrer, error="")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(request.referrer)
