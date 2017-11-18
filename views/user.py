# -*- coding: utf-8 -*-
from flask import g
from flask_login import current_user, login_user, logout_user, login_required

from app import app, login_manager
from models.user import User


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        login_page = LoginPage().set_referrer(request.referrer)
        if user:
            form_password = request.form['password'].encode('utf-8')
            if bcrypt.checkpw(form_password, user.password):
                login_user(user, remember=True)
                app.logger.debug('Logged in user %s', user.username)
                return redirect(request.form['referrer'])
            else:
                login_page.set_form(request.form)
                return login_page.wrong('password').render()
        else:
            return login_page.wrong('username').render()
    return LoginPage().set_referrer(request.referrer).render()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(request.referrer)


@app.route('/edit_user')
@app.route('/edit_user/<user_id>')
@login_required
def user_handler(**kwargs):
    return UserEdit(data=kwargs).render()


@app.route('/api/save_user', methods=['POST', ])
@login_required
def api_save_user():
    user_dict = request.form.to_dict()
    user = save_user(user_dict)
    return redirect('/edit_user/%d' % user.id)


@app.route('/api/delete_user/<user_id>')
@login_required
def api_delete_user(**kwargs):
    delete_user(kwargs['user_id'])
    return redirect(request.referrer)
