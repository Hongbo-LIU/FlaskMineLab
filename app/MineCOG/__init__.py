from flask import Blueprint

MineCOG = Blueprint('MineCOG', __name__)

from . import views   # authentication, posts, users, comments,
