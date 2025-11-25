from app.routes import job_bp
from app.controllers.job_controller import (
    get_all_jobs, create_job, apply_for_job, 
    get_my_applications, delete_application
)
from app.utils.decorators import admin_required
from flask_jwt_extended import jwt_required

# Public Route: Search and List Jobs
job_bp.route('/', methods=['GET'])(get_all_jobs)

# Admin Route: Create Job
job_bp.route('/', methods=['POST']) \
    (jwt_required()(admin_required(create_job)))

# Applicant Routes
job_bp.route('/<int:job_id>/apply', methods=['POST']) \
    (jwt_required()(apply_for_job))

job_bp.route('/my-applications', methods=['GET']) \
    (jwt_required()(get_my_applications))

job_bp.route('/<int:job_id>/application', methods=['DELETE']) \
    (jwt_required()(delete_application))