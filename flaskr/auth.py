


# 4.1 Create a Blueprint 

	# a blueprint is a way to organize a group of related views
	# register your views with the blueprint
	# register the blueprint with the app

	

import functools

from flask import (

    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth') # my authentication blueprint
