# app/routes/__init__.py
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
job_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

# Import the route files effectively
from .auth_routes import *
from .job_routes import *