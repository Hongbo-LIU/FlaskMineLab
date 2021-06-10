from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User
from errors import forbidden, unauthorized
from . import api

auth = HTTPBasicAuth


@auth.verify_password
def verify_password(email, password):
    if email == '':
        return False
    user = User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user = user
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials!')


@api.before_request
@auth.login_required
def before_request():
    if not g.curret_user.is_anonymous and not g.current_user.confirmed:
        return forbidden('Unconfirmed account!')


@api.route('tokens', methods=['GET', 'POST'])
def get_token():
    if g.current_uer.is_anonymous and g.toekn_used:
        return unauthorized('Invalid Credentials!')
    return jsonify({'token': g.current_user.generate_auth_token(expiration=3600), 'expiration': 3600})
