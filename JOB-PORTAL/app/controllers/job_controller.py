# app/controllers/job_controller.py
from flask import request, jsonify
from app.extensions.db import db
from app.models.job import Job
from app.models.application import Application
from flask_jwt_extended import get_jwt_identity

# --- HELPER FUNCTIONS (To replace Schemas) ---
def serialize_job(job):
    return {
        "id": job.id,
        "title": job.title,
        "description": job.description,
        "location": job.location,
        "salary": job.salary,
        "created_at": job.created_at.isoformat() if job.created_at else None
    }

def serialize_application(app, job):
    return {
        "id": app.id,
        "user_id": app.user_id,
        "job_id": app.job_id,
        "applied_at": app.applied_at.isoformat() if app.applied_at else None,
        "job_details": serialize_job(job)
    }

# --- CONTROLLERS ---

def get_all_jobs():
    search_query = request.args.get('q')
    
    if search_query:
        jobs = Job.query.filter(
            (Job.title.ilike(f'%{search_query}%')) | 
            (Job.location.ilike(f'%{search_query}%'))
        ).all()
    else:
        jobs = Job.query.all()
        
    return jsonify([serialize_job(job) for job in jobs]), 200

def create_job():
    data = request.get_json()
    new_job = Job(
        title=data['title'],
        description=data['description'],
        location=data['location'],
        salary=data.get('salary')
    )
    db.session.add(new_job)
    db.session.commit()
    return jsonify(serialize_job(new_job)), 201

def apply_for_job(job_id):
    user_id = get_jwt_identity()
    job = Job.query.get_or_404(job_id)
    
    existing_application = Application.query.filter_by(user_id=user_id, job_id=job_id).first()
    if existing_application:
        return jsonify({"message": "You have already applied for this job"}), 400

    new_application = Application(user_id=user_id, job_id=job_id)
    db.session.add(new_application)
    db.session.commit()
    
    return jsonify({"message": f"Successfully applied for {job.title}"}), 201

def get_my_applications():
    user_id = get_jwt_identity()
    # Join Application and Job to get details in one query
    results = db.session.query(Application, Job)\
        .join(Job, Application.job_id == Job.id)\
        .filter(Application.user_id == user_id).all()
    
    output = []
    for application, job in results:
        output.append(serialize_application(application, job))

    return jsonify(output), 200

def delete_application(job_id):
    user_id = get_jwt_identity()
    application = Application.query.filter_by(user_id=user_id, job_id=job_id).first()
    
    if not application:
        return jsonify({"message": "Application not found"}), 404

    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application withdrawn successfully"}), 200